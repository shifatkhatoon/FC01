
from Find_Blog_data.models.BlogTable import Blogs, Image
from flask import jsonify

def blog_table_add(blog):
    Blog_data = Blogs.query.filter_by(blog_url=blog['url']).first()
    if not Blog_data:
        ImgData = blog.pop("image_url")
        Blog_data = Blogs(blog)
        Blog_data.save()
        for img_url in ImgData:
            Blog_image = Image(img_url, Blog_data.id)
            Blog_image.save()

    return jsonify({'success': 'blog data added'})
