import requests
from bs4 import BeautifulSoup
import csv
import datetime

def search_google(keyword, search_type="inalltitle"):
    """
    Search Google with the given keyword and search type.
    :param keyword: The keyword to search for.
    :param search_type: The type of search ('inalltitle' or 'intitle').
    :return: The number of results found or None if it fails.
    """
    search_url = f"https://www.google.com/search?q={search_type}:{keyword}"
    search_url = f"https://www.google.com/search?q={search_type}:\"{keyword}\""
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        result_stats = soup.find("div", {"id": "result-stats"})
        if result_stats:
            result_text = result_stats.get_text()
            count = result_text.split('About')[1].split('results')[0].strip()
            return count
        else:
            print(f"Could not find result count for {search_type}:{keyword}.")
            return None
    else:
        print(f"Failed to retrieve data for {search_type}:{keyword}")
        return None


def save_to_csv(data, filename="google_search_counts.csv"):
    """
    Save the keyword search results to a CSV file.
    :param data: A list containing the keyword and result counts.
    :param filename: The name of the CSV file to write to.
    """
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def read_keywords_from_csv(platform, filter_option):
    """
    Read keywords from a previous Wayback Machine result CSV file based on naming convention.
    :param platform: The platform name for the file (e.g., 'google').
    :param filter_option: The filter applied (e.g., 'all').
    :return: A list of keywords.
    """
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    input_filename = f"results/{platform}_{filter_option}_{current_date}.txt"

    keywords = []
    try:
        with open(input_filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    keywords.append(row[0])  # Assuming the first column is the keyword
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    return keywords


if __name__ == "__main__":
    platform = "google"  # Replace with the appropriate platform name
    filter_option = "all"  # Replace with the appropriate filter option

    keywords = read_keywords_from_csv(platform, filter_option)

    if keywords:
        for keyword in keywords:
            print(f"Searching for '{keyword}'...")
            inalltitle_count = search_google(keyword, search_type="inalltitle")
            intitle_count = search_google(keyword, search_type="intitle")
            if inalltitle_count and intitle_count:
                save_to_csv([keyword, inalltitle_count, intitle_count])
                print(f"Saved: {keyword} - inalltitle: {inalltitle_count}, intitle: {intitle_count}")
            else:
                print(f"Could not retrieve data for: {keyword}")
    else:
        print("No keywords found to search.")
