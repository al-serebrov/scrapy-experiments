# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class AutoRiaPipeline(object):
    def open_spider(self, spider):
        self.file = open('items.csv', 'w')
        # fieldnames = ['brand', 'model', 'author_name', 'author_phone', 'price',
        #        'city', 'mileage', 'year']
        # fieldnames = {
        #         'brand' : 'Brand',
        #         'model': 'Model',
        #         'author_name': 'Author Name',
        #         'author_phone': 'Phone',
        #         'price': 'Price',
        #         'city': 'City',
        #         'mileage': 'Mileage',
        #         'year': 'Year'
        # }
        # fieldnames = item.fields.keys()
        # self.writer = csv.DictWriter(self.file, delimiter=',', fieldnames=fieldnames)
        # self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        fieldnames = item.keys()
        self.writer = csv.DictWriter(self.file, delimiter=',',
                fieldnames=fieldnames)
        self.writer.writeheader()
        self.writer.writerow(item)
        return item
