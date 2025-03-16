import requests
from bs4 import BeautifulSoup
import re


def fetch(link):
    url = link

    # Extract keyword from the URL using regex
    keyword = re.search(r"stream/([^/]+)", url)
    if keyword:
        keyword = keyword.group(1)

    # Use sets to store filtered links for uniqueness
    filtered_seasons = set()
    filtered_episodes = set()
    episode_link = set()

    # Get the main page content
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all links on the main page
    links = soup.find_all('a')

    # Filter links based on the keyword and append to filtered_seasons
    for link in links:
        href = link.get('href')
        if href and keyword in href and 'episode' not in href:  # Exclude 'episode' in the season links
            filtered_seasons.add(f"https://s.to/{href}")

    # Process each filtered season
    for season_url in filtered_seasons:
        response = requests.get(season_url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all episode links within the season
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href and keyword in href and 'episode' in href:  # Ensure the link contains 'episode'
                filtered_episodes.add(f"https://s.to/{href}")

    for episode_url in sorted(filtered_episodes):
        response = requests.get(episode_url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all episode links with the class "watchEpisode"
        link = soup.find('a', class_='watchEpisode')

        if link:
            h4_tag = link.find('h4')
            if h4_tag and h4_tag.text.strip() == 'VOE':
                href = link.get('href')
                if href:
                    episode_link.add(f"https://s.to{href}")
    return(episode_link)
