from Find_Blog_data import db
from Find_Blog_data.models.base import Base

class Blogs(Base):
    blog_url = db.Column(db.String(100))
    blog_title = db.Column(db.String(200))
    blog_imageUrl = db.relationship('Image', backref='Blogs', lazy=True)
    blog_Author_Name = db.Column(db.String(50))
    blog_Posted_Date = db.Column(db.String(10))
    blog_Content = db.Column(db.String(length=None))

    def __init__(self, blog):
        self.blog_url = blog['url']
        self.blog_title = blog['title']
        self.blog_Author_Name = blog['author']
        self.blog_Posted_Date = blog['posted_date']
        self.blog_Content = blog['content']

    def __repr__(self):
        return '<%s%s%s%s%s%s>' %(self.blog_title,self.blog_url,self.blog_imageUrl,self.blog_Author_Name,
                                  self.blog_Posted_Date, self.blog_Content)

class Image(db.Model):
    Blogs_id = db.Column(db.Integer, db.ForeignKey('Blogs.id'), nullable=False)
    blog_ImageUrl = db.Column(db.String(500))

    def __init__(self,url,blog_id):
        self.Blogs_id = blog_id
        self.blog_ImageUrl = url
    

