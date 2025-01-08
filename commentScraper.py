import requests
from bs4 import BeautifulSoup
import praw
import getpass
import datetime
from pathlib import Path
import configparser
import os
import time
from typing import List, Optional
import logging
from tqdm import tqdm

class RedditScraper:
    def __init__(self, config_path: str = "config.ini"):
        """Initialize the Reddit scraper with configuration."""
        self.config_path = Path(config_path)
        self.setup_logging()
        self.config = self.load_config()
        self.reddit = self.authenticate()

    def setup_logging(self):
        """Set up logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('scraper.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def load_config(self) -> configparser.ConfigParser:
        """Load or create configuration file."""
        config = configparser.ConfigParser()
        
        if not self.config_path.exists():
            config["REDDIT"] = {
                "client_id": input("Enter client ID: "),
                "client_secret": input("Enter client secret: "),
                "username": input("Enter Reddit username: "),
                "password": getpass.getpass("Enter Reddit password: "),
            }
            with open(self.config_path, "w") as f:
                config.write(f)
            self.logger.info(f"Created new config file at {self.config_path}")
        else:
            config.read(self.config_path)
            self.logger.info("Loaded existing config file")
            
        return config

    def authenticate(self) -> praw.Reddit:
        """Authenticate with Reddit API."""
        try:
            reddit = praw.Reddit(
                client_id=self.config["REDDIT"]["client_id"],
                client_secret=self.config["REDDIT"]["client_secret"],
                username=self.config["REDDIT"]["username"],
                password=self.config["REDDIT"]["password"],
                user_agent="Comment Scraper v1.0"
            )
            self.logger.info("Successfully authenticated with Reddit")
            return reddit
        except Exception as e:
            self.logger.error(f"Authentication failed: {str(e)}")
            raise

    def format_comment(self, comment: praw.models.Comment) -> str:
        """Format a single comment with metadata."""
        return (
            f"Comment ID: {comment.id}\n"
            f"Content: {comment.body}\n"
            f"Subreddit: {comment.subreddit_name_prefixed}\n"
            f"Date: {datetime.datetime.fromtimestamp(comment.created_utc)}\n"
            f"Score: {comment.score}\n"
            f"{'-'*80}\n"
        )

    def scrape_comments(self, username: str, limit: Optional[int] = None) -> List[str]:
        """Scrape comments for a given username with error handling and rate limiting."""
        comments = []
        try:
            redditor = self.reddit.redditor(username)
            comment_iterator = redditor.comments.new(limit=limit)
            
            # Get total number of comments for progress bar if no limit is set
            if limit is None:
                try:
                    limit = sum(1 for _ in redditor.comments.new(limit=None))
                except Exception:
                    limit = 100  # fallback value
            
            with tqdm(total=limit, desc="Scraping comments") as pbar:
                for comment in comment_iterator:
                    try:
                        formatted_comment = self.format_comment(comment)
                        comments.append(formatted_comment)
                        pbar.update(1)
                        
                        # Rate limiting
                        time.sleep(0.5)  # Respect Reddit's rate limits
                        
                    except Exception as e:
                        self.logger.warning(f"Error processing comment: {str(e)}")
                        continue
                        
        except Exception as e:
            self.logger.error(f"Error scraping comments: {str(e)}")
            
        return comments

    def save_comments(self, comments: List[str], username: str) -> Path:
        """Save comments to a file with error handling."""
        if not comments:
            self.logger.warning("No comments found to save")
            return None
            
        output_dir = Path("scraped_comments")
        output_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = output_dir / f"{username}_comments_{timestamp}.txt"
        
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("\n".join(comments))
            self.logger.info(f"Saved {len(comments)} comments to {filename}")
            return filename
        except Exception as e:
            self.logger.error(f"Error saving comments: {str(e)}")
            return None

def main():
    scraper = RedditScraper()
    username = input("Enter the Reddit username to scrape: ")
    limit = input("Enter number of comments to scrape (press Enter for all): ")
    limit = int(limit) if limit.strip() else None
    
    comments = scraper.scrape_comments(username, limit)
    scraper.save_comments(comments, username)

if __name__ == "__main__":
    main()
