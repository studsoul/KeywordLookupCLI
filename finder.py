from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'}

postKeyword = input('Enter a keyword for keyword research: ')
gQuery = 'https://www.google.com/?q='% postKeyword

response = requests.get(gQuery)

print('Request sent! Waiting for response.')
