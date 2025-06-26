import requests
from bs4 import BeautifulSoup

# Target news website (you can change this)
URL = 'https://edition.cnn.com/world'

# Send HTTP request
response = requests.get(URL)
if response.status_code != 200:
    print(f"Failed to fetch page: Status code {response.status_code}")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract headlines (CNN typically uses <h3> for headlines)
headlines = soup.find_all(['h2', 'h3'])

# Collect non-empty, cleaned headlines
headline_list = []
for h in headlines:
    text = h.get_text(strip=True)
    if text and len(text) > 10:  # simple filter for quality
        headline_list.append(text)

# Save to a .txt file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for idx, line in enumerate(headline_list, start=1):
        file.write(f"{idx}. {line}\n")

print(f"✅ Scraped and saved {len(headline_list)} headlines to headlines.txt")
