#-*- coding: utf-8 -*-
from flask import request
from Find_Blog_data.api.addToDb import blog_table_add
from Find_Blog_data.schema.Blogschema import BlogSchema
from Find_Blog_data.models.BlogTable import Blogs
from Find_Blog_data import app
from flask import jsonify
import json


@app.route("/blog", methods=['POST', 'GET'])
def add_blogdata():
    if request.method == 'POST':
        blog = request.get_json()
        jsondata = blog_table_add(blog)
        return jsondata
    else:
        per_page = int(request.args.get('per_page', 10))
        page = int(request.args.get('page', 1))
        blogdata = Blogs.query.order_by(Blogs.id.desc()).offset((page - 1) * per_page).limit(per_page).all()
        if blogdata:
            data = BlogSchema(many=True).dump(blogdata).data
            response = jsonify({"result": data})
            return response