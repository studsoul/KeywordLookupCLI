from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'}

postKeyword = input('Enter a keyword for keyword research: ')
gQuery = 'https://www.ask.com/web?q=%s&ad=dirN&qo=homepageSearchBox' % str(postKeyword)
# replaced Google with Ask because Google is blocked
response = requests.get(gQuery, headers=headers)
html_response = response.text
# print(html_response)
soup = BeautifulSoup(html_response, 'html.parser')
relresponse = soup.find_all("span", class_="PartialRelatedSearch-item-link-text")
print("Related Keywords for your Post Idea")
if len(relresponse) == None:
    print("No Related Keywords Found")
else:
    for i in range(len(relresponse)//2):
        print(relresponse[i].text)