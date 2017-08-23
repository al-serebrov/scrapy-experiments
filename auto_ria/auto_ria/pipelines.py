# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class AutoRiaPipeline(object):
    
    headers_check = None

    def open_spider(self, spider):
        self.filename = 'items.csv'
        self.file = open(self.filename, 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if self.headers_check is None:
            with open(self.filename, 'r') as csvfile:
                self.reader = csv.DictReader(csvfile, delimiter=',')
                self.headers_check = self.reader.fieldnames
                fieldnames = item.keys()
                self.writer = csv.DictWriter(self.file, delimiter=',',
                        fieldnames=fieldnames)
                self.writer.writeheader()
        self.writer.writerow(item)
        return item
