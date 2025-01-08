# RedditCommentScraper v1.1.0

A Python script to scrape and save comments from a specified Reddit user using the Reddit API via `praw`.

## Features

- Authenticate with Reddit using your credentials.
- Scrape comments from a specific Reddit user.
- Save comments to a timestamped text file in a structured format.
- Rate-limiting and error handling to comply with Reddit API guidelines.
- Progress bar for tracking scraping progress.

## Prerequisites

- Python 3.8 or higher
- A Reddit account with API credentials (client ID and client secret)
- `praw`, `requests`, `beautifulsoup4`, `tqdm`

## Installation

1. Clone this repository or copy the script into your project directory.
2. Install the required Python packages:
   ```bash
   pip install praw requests beautifulsoup4 tqdm

## Reddit Configuration

1. Navigate to https://www.reddit.com/prefs/apps

2. Click "Create application" at the bottom of the page

3. Select "script"

4. Fill out the discription, and both URL and URI fields (you can point both fields to this Github page)

5. Click 'create app'

![image](https://user-images.githubusercontent.com/130249301/234336730-dbe61b3f-ffed-4f1f-ab35-b5fe1239d72c.png)

## Usage

1. Run the script using:

```bash
python reddit_scraper.py
```

2. View Output: The scraped comments will be saved in a scraped_comments folder, with the filename format:

```bash
<username>_comments_<timestamp>.txt
```

## Configuration

The script creates a config.ini file in the current directory to store your Reddit credentials securely. You can edit this file manually if needed.

## Logging

Logs are saved in a scraper.log file in the current directory and printed to the console. These logs include:

- Authentication status
- Comment scraping progress
- Warnings or errors

## Example Output
Each comment is saved in the following format:
```bash
Comment ID: <id>
Content: <comment body>
Subreddit: <subreddit>
Date: <timestamp>
Score: <score>
--------------------------------------------------------------------------------
```

## License
This project is open-source and available under the MIT License.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance functionality or fix bugs.

## Contact
For any questions or suggestions, please reach out via the Issues tab in this repository.

## Changelog

# v1.1.0

## Added
- Restructured code into RedditScraper class
- Added comprehensive logging system
- Implemented progress bar using tqdm
- Enhanced error handling and recovery
- Added rate limiting
- Improved comment metadata
- Created dedicated output directory
- Added timestamp to output files
- Implemented secure password input
- Added optional comment limit
- Improved configuration management
- Enhanced UTF-8 handling
- Added type hints
- Improved code organization and documentation
- Added detailed logging to file
- Enhanced user experience with better console output
