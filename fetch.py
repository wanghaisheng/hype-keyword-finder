#!/usr/bin/env python3

import requests
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import os
from datetime import datetime, timedelta

# ASCII Art for a visual touch on script execution
ASCII_ART = '''
             |
       Atrax |
             |
         /   |   \
         \   |   /
       .  --\|/--  ,
        '--|___|--'
        ,--|___|--,
       '  /\o o/\  `
         +   +   +
          `     ' 
'''

# Class for defining terminal color codes for enhanced output readability
class TerminalColors:
    OK = '\033[92m'      # Green text
    WARNING = '\033[93m' # Yellow text
    FAIL = '\033[91m'    # Red text
    RESET = '\033[0m'    # Reset to default
    INFO = '\033[94m'    # Blue text

# Constants for API URL and screenshot directory
WAYBACK_API_URL = "https://web.archive.org/cdx/search?matchType=domain&collapse=urlkey&output=text&fl=original"
SCREENSHOT_FOLDER = "screens/"

def setup_arg_parser():
    """ Set up and return the argument parser for command line arguments. """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Target domain (e.g., target.com)", type=str, required=True)
    parser.add_argument("-k", "--keyword", help="Specific extension or keyword (e.g., js, xml, json, pdf, css, admin, login)", type=str)
    parser.add_argument("-l", "--limit", help="Limit (number of links)", type=int)
    parser.add_argument("-s", "--screenshot", help="Take a screenshot of each URL found", action="store_true")
    parser.add_argument("-r", "--rate-limit", help="Delay between screenshots in seconds", type=float, default=1)
    parser.add_argument("-o", "--output", help="Output file path", type=str)
    parser.add_argument("--filter", help="Time filter for Wayback Machine API. Options: last_day, last_7_days, last_30_days", type=str)
    return parser

def take_screenshots(urls, rate_limit):
    """ Take screenshots of the provided URLs using Selenium WebDriver. """
    options = Options()
    options.add_argument('--headless')  # Run browser in headless mode
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(30)    # Timeout for page load
    
    print(TerminalColors.OK + "[+] Screening URLs..." + TerminalColors.RESET)
    for i, url in enumerate(urls.split(), start=1):
        try:
            driver.get(url)
            sleep(rate_limit)  # Wait for specified rate limit
            screenshot_path = f"{SCREENSHOT_FOLDER}screen-{i}.png"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            print(f"Error taking screenshot of {url}: {e}")

    driver.quit()
    print(TerminalColors.OK + "[+] Done with screenshots!" + TerminalColors.RESET)

def fetch_urls(domain, keyword, limit, filter_option):
    """ Fetch URLs from the Wayback Machine API based on the domain, optional keyword, limit, and filter. """
    # Calculate date range based on the filter option
    date_from = ""
    date_to = ""

    if filter_option == "last_day":
        date_from = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
        date_to = datetime.now().strftime("%Y%m%d")
    elif filter_option == "last_7_days":
        date_from = (datetime.now() - timedelta(days=7)).strftime("%Y%m%d")
        date_to = datetime.now().strftime("%Y%m%d")
    elif filter_option == "last_30_days":
        date_from = (datetime.now() - timedelta(days=30)).strftime("%Y%m%d")
        date_to = datetime.now().strftime("%Y%m%d")

    url = f"{WAYBACK_API_URL}&url={domain}/"
    if keyword:
        url += f"&filter=urlkey:.*{keyword}"
    if date_from and date_to:
        url += f"&from={date_from}&to={date_to}"
    if limit:
        url += f"&limit={limit}"
    
    response = requests.get(url)
    return response.text

def save_urls_to_file(urls):
    """ Save the fetched URLs to a file named after the current date. """
    current_date = datetime.now().strftime("%Y-%m-%d")
    file_path = f"wayback_urls_{current_date}.txt"
    with open(file_path, "w") as file:
        file.write(urls)
    print(f"URLs saved to {file_path}")

def main():
    """ Main function to orchestrate the script's functionalities. """
    print(ASCII_ART)
    parser = setup_arg_parser()
    args = parser.parse_args()

    try:
        urls = fetch_urls(args.domain, args.keyword, args.limit, args.filter)
        save_urls_to_file(urls)
        if args.screenshot:
            take_screenshots(urls, args.rate_limit)
    except Exception as e:
        print(TerminalColors.FAIL + f"[!] Error: {e}" + TerminalColors.RESET)

if __name__ == "__main__":
    # Ensure the script only runs when not imported as a module
    try:
        main()
    except KeyboardInterrupt:
        print(TerminalColors.FAIL + "[!] Script canceled by user." + TerminalColors.RESET)
