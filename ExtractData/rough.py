import requests
from bs4 import BeautifulSoup
url = 'https://www.thomascook.com/blog/holidays/city-breaks/best-cities-europe-spend-new-years-eve/'

WebPage = requests.get(url)
soup = BeautifulSoup(WebPage.text, 'lxml')

title = soup.find(attrs={'class': 'post-title single-post-title'}).text
print(title)

Images = []
for img in soup.find_all('img'):
    Images.append(img.get('src'))
print(Images)

authorName = soup.find(attrs={'class': 'author-post'}).text
print(authorName)

Postdate = soup.find(attrs={'class': 'post-box-meta-single'}).text
post_date = Postdate
print(post_date)

content = soup.find(attrs={'class': 'inner-post-entry'})
Content = content.find_all('p')
print(Content)


