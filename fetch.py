#!/usr/bin/env python3

import requests
import datetime
import os
import sys

# Define the hashtag
hashtag = "exampleHashtag"  # Replace with your actual hashtag

# Define the list of links for the given hashtag
links1 = [
    {"Facebook": f"https://www.facebook.com/hashtag/{hashtag}"},
    {"Instagram": f"https://www.instagram.com/explore/tags/{hashtag}"},
    {"Vkontakte": f"https://vk.com/search?c%5Bq%5D=%23{hashtag}&c%5Bsection%5D=statuses"},
    {"myMail": f"https://my.mail.ru/hashtag/{hashtag}"},
    {"Pinterest": f"https://www.pinterest.com/search/pins/?q=%23{hashtag}&rs=typed&term_meta[]=%23{hashtag}%7Ctyped"},
    # Add other platforms as needed...
]
hashtag = "exampleHashtag"  # Replace with your actual hashtag

# Define the list of links for the given hashtag
links = [
    {"Facebook": f"https://www.facebook.com/hashtag/{hashtag}"},
    {"Instagram": f"https://www.instagram.com/explore/tags/{hashtag}"},
    {"Vkontakte": f"https://vk.com/search?c%5Bq%5D=%23{hashtag}&c%5Bsection%5D=statuses"},
    {"myMail": f"https://my.mail.ru/hashtag/{hashtag}"},
    {"Pinterest": f"https://www.pinterest.com/search/pins/?q=%23{hashtag}&rs=typed&term_meta[]=%23{hashtag}%7Ctyped"},
    {"Tumblr": f"https://www.tumblr.com/search/%23{hashtag}"},
    {"Twitter": f"https://twitter.com/search?q=%23{hashtag}&src=typed_query&f=live"},
    {"Telegram": f"https://lyzem.com/search?q=%23{hashtag}"},
    {"Reddit": f"https://www.reddit.com/search/?q=%23{hashtag}"},
    {"Clubhouse": f"https://clubhousedb.com/search-clubs?q=%23{hashtag}"},
    {"Youtube": f"https://www.youtube.com/hashtag/{hashtag}"},
    {"Twitch": f"https://www.twitch.tv/search?term=%23{hashtag}"},
    {"Medium": f"https://medium.com/search?q=%23{hashtag}"},
    {"Livejournal": f"https://www.livejournal.com/rsearch?tags={hashtag}&searchArea=post"},
    {"Yandexzen": f"https://zen.yandex.ru/search?query=%23{hashtag}"},
    {"Baidutieba": f"https://tieba.baidu.com/f/search/res?qw=%23{hashtag}&sm=2&cf=1&ie=utf-8"},
    {"Weibo": f"https://s.weibo.com/weibo?q=%23{hashtag}&Refer=index"},
    {"Yycom": f"https://www.yy.com/search-#{hashtag}"},
    {"Myspace": f"https://myspace.com/search?q=%23{hashtag}"},
    {"Skyrock": f"https://www.skyrock.com/search/articles/?q=%23{hashtag}#gsc.tab=0&gsc.q=%23{hashtag}&gsc.page=1"},
    {"Thriller": f"https://triller.co/search?search=%23{hashtag}"},
    {"Likee": f"https://likee.video/search/%23{hashtag}"},
    {"Fark": f"https://www.fark.com/hlsearch?qq=%23{hashtag}&undefined=Go&is_using_js=1"},
    {"Devianart": f"https://www.deviantart.com/search?q=%23{hashtag}"},
    {"Reverbnation": f"https://www.reverbnation.com/main/search?q=%23{hashtag}"},
    {"Wattpad": f"https://www.wattpad.com/search/%23{hashtag}"},
    {"Soundcloud": f"https://soundcloud.com/search?q=%23{hashtag}"},
    {"Flickr": f"https://www.flickr.com/search/?text=%23{hashtag}"},
    {"Digg": f"https://digg.com/search?q=%23{hashtag}"},
    {"Hubpages": f"https://discover.hubpages.com/search?query=%23{hashtag}"},
    {"Snapchat": f"https://story.snapchat.com/search?q={hashtag}"},
    {"Quora": f"https://www.quora.com/search?q=%23{hashtag}"},
    {"Tiktok": f"https://www.tiktok.com/tag/{hashtag}?lang=en"},
    {"Vimeo": f"https://vimeo.com/search?q=%23{hashtag}"},
    {"Douban": f"https://www.douban.com/search?source=suggest&q=%23{hashtag}"},
    {"Douyin": f"https://www.douyin.com/search/%23{hashtag}?source=normal_search&aid=ae28cade-2fa5-4e16-bc8f-7f06ead531b2&enter_from=main_page"},
    {"Kuaishou": f"https://www.kuaishou.com/search/video?searchKey=%23{hashtag}"},
    {"Piscart": f"https://picsart.com/search?q=%23{hashtag}"},
    {"Girlsaskguys": f"https://www.girlsaskguys.com/search?q=%23{hashtag}"},
    {"Producthunt": f"https://www.producthunt.com/search?q=%23{hashtag}"},
    {"Kikstarter": f"https://www.kickstarter.com/discover/advanced?ref=nav_search&term=%23{hashtag}"},
    {"Fotki": f"https://search.fotki.com/?q=%23{hashtag}"},
    {"Bilibili": f"https://search.bilibili.com/all?keyword=%23{hashtag}&from_source=webtop_search"},
    {"Ixigua": f"https://www.ixigua.com/search/%23{hashtag}"},
    {"Huya": f"https://www.huya.com/search?hsk=%23{hashtag}"},
    {"Meipai": f"https://www.meipai.com/search/all?q=%23{hashtag}"},
    {"Gofundme": f"https://www.gofundme.com/s?q=%23{hashtag}"},
    {"Dribbble": f"https://dribbble.com/search/#" + hashtag},
    # Add other links as needed
]

links=[

        {"Facebook": f"https://www.facebook.com/hashtag/{hashtag}"},
    {"Tiktok": f"https://www.tiktok.com/tag/{hashtag}?lang=en"},
    {"Douyin": f"https://www.douyin.com/search/%23{hashtag}?source=normal_search&aid=ae28cade-2fa5-4e16-bc8f-7f06ead531b2&enter_from=main_page"},
    {"Youtube": f"https://www.youtube.com/hashtag/{hashtag}"},
    {"Quora": f"https://www.quora.com/search?q=%23{hashtag}"},
    {"Kikstarter": f"https://www.kickstarter.com/discover/advanced?ref=nav_search&term=%23{hashtag}"},

]

# Print all links
for link in links:
    for platform, url in link.items():
        print(f"{platform}: {url}")
# Wayback Machine API base URL
WAYBACK_API_URL = "https://web.archive.org/cdx/search?matchType=domain&collapse=urlkey&output=text&fl=original"

# Function to calculate the timestamp for a given number of days ago
def get_timestamp_for_days_ago(days):
    return (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y%m%d%H%M%S")

# Function to fetch Wayback URLs for a given base URL and date range filter
def fetch_wayback_urls(base_url, days_filter):
    """ Fetch URLs from Wayback Machine based on the base URL and a date filter. """
    # Get the timestamp for the date range
    if days_filter == '30_days':
        timestamp = get_timestamp_for_days_ago(30)
    elif days_filter == '7_days':
        timestamp = get_timestamp_for_days_ago(7)
    elif days_filter == '1_day':  # Default filter
        timestamp = get_timestamp_for_days_ago(1)
    else:
        raise ValueError("Invalid filter. Choose '30_days', '7_days', or '1_day'.")

    # Construct the API URL with the timestamp filter
    url = f"{WAYBACK_API_URL}&url={base_url}/&timestamp={timestamp}"
    response = requests.get(url)
    return response.text

# Function to save the fetched URLs to a file
def save_to_file(platform, filter_option, data):
    """ Save the fetched data to a file with a name that includes the platform, filter option, and current date. """
    # Get today's date in YYYY-MM-DD format
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Create a filename based on platform, filter, and date
    filename = f"results/{platform}_{filter_option}_{current_date}.txt"
    
    # Ensure the results directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Open the file in append mode and write the data
    with open(filename, "a") as file:
        file.write(f"Results for {platform} ({filter_option}) on {current_date}:\n")
        file.write(data)
        file.write("\n\n")  # Add spacing between different results

    print(f"Results saved to {filename}")

# Main function to process the links and fetch archived URLs from Wayback Machine
def process_links(filter_option):
    # Process each link
    for link in links:
        for platform, url in link.items():
            base_url = url.split(f"%23{hashtag}")[0]  # Extract the part before the hashtag
            print(f"Fetching Wayback Machine URLs for {platform}: {base_url}")
            
            # Fetch and save the result from Wayback Machine API
            try:
                wayback_urls = fetch_wayback_urls(base_url, filter_option)
                save_to_file(platform, filter_option, wayback_urls)
            except Exception as e:
                print(f"Error fetching data for {platform}: {e}")

# Read the filter option from the command-line arguments (passed from GitHub Actions)
filter_option = sys.argv[1] if len(sys.argv) > 1 else '1_day'  # Default to '1_day'

# Call the main function
process_links(filter_option)
