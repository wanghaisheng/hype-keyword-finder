import requests
from bs4 import BeautifulSoup
import csv

def search_google(keyword, search_type="inalltitle"):
    """
    Search Google with the given keyword and search type.
    :param keyword: The keyword to search for.
    :param search_type: The type of search ('inalltitle' or 'intitle').
    :return: The number of results found or None if it fails.
    """
    # Define the search URL based on the search type (inalltitle or intitle)
    search_url = f"https://www.google.com/search?q={search_type}:{keyword}"

    # Set user-agent header to simulate a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send the GET request to Google search
    response = requests.get(search_url, headers=headers)

    # If the request was successful, parse the content
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the div with id="result-stats"
        result_stats = soup.find("div", {"id": "result-stats"})
        
        if result_stats:
            # Extract the text and clean it to get the count
            result_text = result_stats.get_text()
            # Example: "About 4 results"
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


def read_keywords_from_csv(input_filename):
    """
    Read keywords from a previous Wayback Machine result CSV file.
    :param input_filename: The name of the CSV file containing Wayback Machine results.
    :return: A list of keywords.
    """
    keywords = []
    try:
        with open(input_filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming the first column of the CSV is the keyword
                if row:
                    keywords.append(row[0])  # Adjust index if necessary
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    return keywords


if __name__ == "__main__":
    # Read keywords from the Wayback Machine result CSV file
    input_filename = 'waybackmachine_results.csv'  # Change this to your actual filename
    keywords = read_keywords_from_csv(input_filename)

    if keywords:
        # Loop through each keyword
        for keyword in keywords:
            print(f"Searching for '{keyword}'...")
            
            # Fetch the search count for 'inalltitle'
            inalltitle_count = search_google(keyword, search_type="inalltitle")
            
            # Fetch the search count for 'intitle'
            intitle_count = search_google(keyword, search_type="intitle")
            
            if inalltitle_count and intitle_count:
                # Save keyword and both counts to CSV
                save_to_csv([keyword, inalltitle_count, intitle_count])
                print(f"Saved: {keyword} - inalltitle: {inalltitle_count}, intitle: {intitle_count}")
            else:
                print(f"Could not retrieve data for: {keyword}")
    else:
        print("No keywords found to search.")
