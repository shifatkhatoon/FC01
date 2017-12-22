# -*- coding: utf-8 -*-
from Find_Blog_data import ma


class BlogSchema(ma.Schema):
    image = ma.Nested(ImageSchema, many=True, exclude=('id', 'created_at', 'updated_at'))

    class Meta:
        fields = ('id', 'created_at', 'updated_at', 'title', 'url',
                  'author', 'posted_date', 'content')
        exclude = ('created_at', 'updated_at', 'id')


blog_schema = BlogSchema()
blog_schema = BlogSchema(many=True)


class ImageSchema(ma.Schema):
    class Relation:
        fields = ('id', 'created_at', 'updated_at', 'Blogs_id', 'blog_Imageurl')
