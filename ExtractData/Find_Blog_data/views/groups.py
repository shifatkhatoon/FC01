# -*- coding: utf-8 -*-
# from flask import request
# from Find_Blog_data.api.groups import group_add
# from Find_Blog_data.schema.groups import group_schema
# from Find_Blog_data.models.BlogTable import Blogs
# from Find_Blog_data import app
# from flask import Response
# import json
#
#
# @app.route("/group", methods=['POST', 'GET'])
# def add_group():
#     if request.method == 'POST':
#         data = request.get_json()
#         jsondata = group_add(data)
#         return jsondata
#     else:
#         per_page = int(request.args.get('per_page', 10))
#         page = int(request.args.get('page', 1))
#         groups = Blogs.query.order_by(Blogs.id.desc()).offset((page - 1) * per_page).limit(per_page).all()
#
#         return group_schema.jsonify(groups)

