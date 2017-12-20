# -*- coding: utf-8 -*-
from flask_script import Command
from Find_Blog_data.utils.Urls import extracturls
from Find_Blog_data.api.addToDb import blog_table_add
from Find_Blog_data.library.BlogData import finddata


class Addblog(Command):
    def run(self):
        print("Adding Blog")
        urls = extracturls()
        print(len(urls))
        for url in urls:
            Object = finddata(url)
            dictionary = Object.getdict()

