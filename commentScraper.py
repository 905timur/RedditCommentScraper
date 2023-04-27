import requests
from bs4 import BeautifulSoup
import praw
import getpass
import datetime
import configparser
import os
import time

# Check if the config file exists, create one if it doesn't
config = configparser.ConfigParser()
if not os.path.exists("config.ini"):
    config["REDDIT"] = {
        "client_id": "",
        "client_secret": "",
        "username": "",
        "password": "",
    }
    with open("config.ini", "w") as f:
        config.write(f)

# Read the config file
config.read("config.ini")
client_id = config["REDDIT"]["client_id"]
client_secret = config["REDDIT"]["client_secret"]
username = config["REDDIT"]["username"]
password = config["REDDIT"]["password"]

# Prompt the user for the Reddit username of the user to scrape
reddit_username = input("Enter the Reddit username you want to scrape: ")

# Authenticate with the Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent="scraper",
)

# Get the user's comments
comments = []
new_comments = reddit.redditor(reddit_username).comments.new(limit=None)

# Print Working... animation
print("Working", end="", flush=True)
while True:
    try:
        new_comment = next(new_comments)
        comment_text = f"{new_comment.body}\n\n{new_comment.subreddit_name_prefixed} - {datetime.datetime.fromtimestamp(new_comment.created_utc)}\n{'-'*80}\n"
        comments.append(comment_text)
        print(".", end="", flush=True)
    except StopIteration:
        break
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Saving comments...", flush=True)
        break
    except Exception as e:
        print(f"\n\nError: {e}. Trying again in 5 seconds...", flush=True)
        time.sleep(5)

# Check if any comments were scraped
if len(comments) == 0:
    print("\n\nNo comments found for this user.", flush=True)
else:
    # Save the comments to a text file
    filename = f"{reddit_username}_comments.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(comments))
    print(f"\n\nSaved {len(comments)} comments to {filename}", flush=True)
