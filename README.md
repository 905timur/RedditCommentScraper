# RedditCommentScraper v1.0


This Python script scrapes the entire history of any Reddit user and saves it to a text file in the same directory.


**-SYSTEM CONFIGURATION-**

1. Install Python 3

2. Install praw and beautifulsoup4 by running the following code in terminal:

```
pip install praw
```
Do the same command for beautifulsoup4


**-REDDIT CONFIGURATION-**

1. Navigate to https://www.reddit.com/prefs/apps

2. Click "Create application" at the bottom of the page

3. Select "script"

4. Fill out the discription, and both URL and URI fields (you can point both fields to this Github page)

5. Click 'create app'

![image](https://user-images.githubusercontent.com/130249301/234336730-dbe61b3f-ffed-4f1f-ab35-b5fe1239d72c.png)


**-SCRIPT CONFIGURATION-**

1. Add the client ID, secret, username and password to the config.ini file

2. Make sure both the scraper and the config files are in the same directory. 

**-SCRIPT EXECUTION-**

1. In your Windows terminal navigate to the directory where the script and the config files are saved, for example:


```
cd C:\commentScraper
```

2. Execute the script:


```
python commentScraper.py
```

3. Input the username you want to scrape and hit enter. 
