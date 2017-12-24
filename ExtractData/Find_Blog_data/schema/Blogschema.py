# -*- coding: utf-8 -*-
from Find_Blog_data import ma
from Find_Blog_data.models.BlogTable import Image


class ImageSchema(ma.Schema):
    class Meta:
        fields = [('blog_ImageUrl')]
        exclude = ('created_at', 'updated_at', 'id')
class BlogSchema(ma.Schema):
    blog_imageUrl = ma.Nested(ImageSchema,many=True)
    class Meta:
        fields = ('blog_title', 'blog_url',
                 'blog_Author_Name', 'blog_Posted_Date', 'blog_Content','blog_imageUrl')
        exclude = ('created_at', 'updated_at', 'id')


blog_schema = BlogSchema()
blog_schema = BlogSchema(many=True)


