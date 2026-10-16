#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
import sys

# Ask the user for input
url = input("Enter the URL to scrape: ")
min_length = int(input("Enter minimum word length: "))
max_length = int(input("Enter maximum word length: "))
output_file = input("Enter output filename (e.g. output.txt): ")

# Download the webpage
response = requests.get(url, timeout=15)

if response.status_code != 200:
    print("Error fetching the webpage.")
    sys.exit(1)

# Parse the HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extract webpage text
text = soup.get_text()

# Extract words using regex
words = re.findall(r"\b\w+\b", text)

# Filter words by length
filtered_words = [
    word for word in words
    if min_length <= len(word) <= max_length
]

# Save the words to a file
with open(output_file, "w", encoding="utf-8") as file:
    for word in filtered_words:
        file.write(word + "\n")

print(f"Saved {len(filtered_words)} words to {output_file}")
