import scrapy
from collections import OrderedDict

class QuotesSpider(scrapy.Spider):
    name = "auto_ria"
    start_urls = [
        'https://auto.ria.com/auto_renault_trafic_gruz_20244222.html',
        'https://auto.ria.com/auto_renault_trafic_gruz_19265168.html',
    ]

    def parse(self, response):
        params = {
            'brand': response.css('span[itemprop="brand"]::text').extract_first(),
            'model': response.css('span[itemprop="name"]::text').extract_first(),
            'author_name':
                response.css('dt.user-name strong::text').extract_first(),
            'author_phone':
                response.css('span.mhide::attr(data-phone-number)').extract_first(),
            'price': response.css('span.price::text').extract_first(),
            'city':
                response.css('span[title="Город продавца"]::text').extract_first(),
            'mileage': response.css('div.run strong::text').extract_first(),
            'year': response.css('span.year::text').extract_first()
        }
        yield OrderedDict(params)
