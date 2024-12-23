#!/usr/bin/env python3

import requests
import datetime
import os
import sys
from waybackpy import WaybackMachineCDXServerAPI

# Define the hashtag
hashtag = "exampleHashtag"  # Replace with your actual hashtag

# Define the list of links for the given hashtag
links = [
    {"Facebook": f"https://www.facebook.com/hashtag/{hashtag}"},
    {"Tiktok": f"https://www.tiktok.com/tag/{hashtag}?lang=en"},
    {"Douyin": f"https://www.douyin.com/search/%23{hashtag}?source=normal_search&aid=ae28cade-2fa5-4e16-bc8f-7f06ead531b2&enter_from=main_page"},
    {"Youtube": f"https://www.youtube.com/hashtag/{hashtag}"},
    {"Quora": f"https://www.quora.com/search?q=%23{hashtag}"},
    {"Kickstarter": f"https://www.kickstarter.com/discover/advanced?ref=nav_search&term=%23{hashtag}"},
]

# Wayback Machine API base URL
WAYBACK_API_URL = "https://web.archive.org/cdx/search?matchType=domain&collapse=urlkey&output=text&fl=original"

# Function to calculate the start and end timestamps for a given timeframe
def get_time_range(filter_option):
    now = datetime.datetime.now()
    if filter_option == '30_days':
        start = (now - datetime.timedelta(days=30)).strftime("%Y%m%d%H%M%S")
    elif filter_option == '7_days':
        start = (now - datetime.timedelta(days=7)).strftime("%Y%m%d%H%M%S")
    elif filter_option == '1_day':
        start = (now - datetime.timedelta(days=1)).strftime("%Y%m%d%H%M%S")
    else:
        raise ValueError("Invalid filter. Choose '30_days', '7_days', or '1_day'.")
    end = now.strftime("%Y%m%d%H%M%S")
    return start, end

# Function to fetch Wayback URLs for a given base URL and date range filter
def fetch_wayback_urls1(base_url, filter_option):
    """Fetch URLs from Wayback Machine based on the base URL and a date range."""
    # Get the start and end timestamps for the date range
    start, end = get_time_range(filter_option)

    # Construct the API URL with the start and end timestamps
    url = f"{WAYBACK_API_URL}&url={base_url}/&from={start}&to={end}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP issues
    return response.text
def fetch_wayback_urls(base_url, filter_option):
    start, end = get_time_range(filter_option)
    user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    print('========',start,end,base_url)
    cdx = WaybackMachineCDXServerAPI(base_url, user_agent,
                                            match_type="prefix",
         collapses=["urlkey"],

                                     start_timestamp=start, end_timestamp=end)
    urls=[]
    for item in cdx.snapshots():
        print('-------'.item)
        url=item.archive_url
        urls.append(url)
    
    
    # Function to save the fetched URLs to a file
def save_to_file(platform, filter_option, data):
    """Save the fetched data to a file with a name that includes the platform, filter option, and current date."""
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
