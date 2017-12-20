import requests
from bs4 import BeautifulSoup

class finddata():

    def __init__(self, url):
        self.BlogData = {}
        WebPage = requests.get(url)
        self.soup = BeautifulSoup(WebPage.text, 'lxml')

    def geturl(self):
        self.url = self.soup.find(attrs={'rel': 'canonical'}).get('href')
        return self.url

    def gettitle(self):
        self.title = self.soup.find(attrs={'class': 'post-title single-post-title'}).text
        return self.title

    def getimage(self):
        self.Images = []
        for img in self.soup.find_all('img'):
            self.Images.append(img.get('src'))
        return self.Images

    def getdate(self):
        self.Postdate = self.soup.find(attrs={'class': 'post-box-meta-single'})
        self.Getboth = self.Postdate.text
        self.post_date = self.Getboth.split('\n')[2]
        return self.post_date

    def getauthor(self):
        self.authorName = self.soup.find(attrs={'class': 'author-url'}).text
        return self.authorName

    def getcontent(self):
        self.content = self.soup.find(attrs={'class': 'inner-post-entry'}).text
        return self.content

    def getdict(self):
        self.BlogData['url'] = self.geturl()
        self.BlogData['title'] = self.gettitle()
        self.BlogData['image_url'] = self.getimage()
        self.BlogData['author'] = self.getauthor()
        self.BlogData['posted_date'] = self.getdate()
        self.BlogData['content'] = self.getcontent()
        return self.BlogData
