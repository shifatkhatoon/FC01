# -*- coding: utf-8 -*-
from flask_script import Command
from Find_Blog_data.utils.Urls import extracturls
from Find_Blog_data.api.addToDb import blog_table_add
from Find_Blog_data.library.BlogData import Finddata


class Addblog(Command):
    def run(self):
        count = 0
        print("Adding Blog")
        urls = extracturls()
        print(len(urls))
        for url in urls:
            count += 1
            print(count)
            print(url)
            try:
                Object = Finddata(url)
                dictionary = Object.getdict()
                blog_table_add(dictionary)
            except Exception as e:
                print("Url {0} has Error {1}".format(url, e))
