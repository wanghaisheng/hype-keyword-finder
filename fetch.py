#!/usr/bin/env python3

import requests
import datetime
import os
import sys
import links from ./urls

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
