import requests
from bs4 import BeautifulSoup


# Function to extract article numbers from a given URL
def extract_article_number(url):
    try:
        # Fetch the HTML content of the page
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        html_content = response.text

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Search for the "Art.nr" label and extract the number next to it
        # soup.find_parent(text=re.compile("Art\.nr"))
        label = soup.find("strong", string="Art.nr:")
        if label:
            value_tag = label.find_next_sibling("span")
            if value_tag:
                return value_tag.get_text()
    except Exception as e:
        print(f"Error processing URL {url}: {e}")
    return None
