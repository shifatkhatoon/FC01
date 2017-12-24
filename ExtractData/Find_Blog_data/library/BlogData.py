import requests
from bs4 import BeautifulSoup
import time


class Finddata():
    def __init__(self, url):
        self.url = url
        self.BlogData = {}
        try:
            WebPage = requests.get(url)
            self.soup = BeautifulSoup(WebPage.text, 'lxml')
            print("open page")
        except:
            time.sleep(10)
            self.x = set(url)
            Finddata(self.x)

    def geturl(self):
        try:
            self.urls = self.soup.find(attrs={'rel': 'canonical'}).get('href')
            return self.urls
        except AttributeError:
            return self.url

    def gettitle(self):
        try:
            self.title = self.soup.find(attrs={'class': 'post-title single-post-title'}).text
            return self.title
        except AttributeError:
            self.title = self.soup.find(attrs={'class': 'where-main-title '}).text
            return self.title

    def getimage(self):
        try:
            self.Images = []
            for img in self.soup.find_all('img'):
                self.Images.append(img.get('src'))
            return self.Images
        except AttributeError:
            self.Images = self.soup.find(attrs={'class': 'cta-btn view-forecast-link'}).get('href')
            return self.Images

    def getdate(self):
        try:
            self.Postdate = self.soup.find(attrs={'class': 'post-box-meta-single'})
            self.Getboth = self.Postdate.text
            self.post_date = self.Getboth.split('\n')[2]
            return self.post_date
        except AttributeError:
            return "None"

    def getauthor(self):
        try:
            self.authorName = self.soup.find(attrs={'class': 'author-url'}).text
            return self.authorName
        except AttributeError:
            return "None"

    def getcontent(self):
        try:
            self.content = self.soup.find(attrs={'class': 'inner-post-entry'}).text
            return self.content
        except AttributeError:
            self.content = self.soup.find(attrs={'class': 'where-content-text'}).text
            return self.content

    def getdict(self):
        self.BlogData['url'] = self.geturl()
        self.BlogData['title'] = self.gettitle()
        self.BlogData['image_url'] = self.getimage()
        self.BlogData['author'] = self.getauthor()
        self.BlogData['posted_date'] = self.getdate()
        self.BlogData['content'] = self.getcontent()
        print("get dict")
        return self.BlogData
