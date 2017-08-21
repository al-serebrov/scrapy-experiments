import scrapy
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = "auto_ria"
    search_url = 'https://auto.ria.com/search/?category_id=1&marka_id[0]=84&model_id[0]=31495&s_yers[0]=2003&po_yers[0]=2004&currency=1&abroad=2&custom=1&fuelRatesType=city&engineVolumeFrom=&engineVolumeTo=&power_name=1&countpage=10'
    start_urls = []
    page_counter = 1


    def find_urls(self, url):
        """Find all ads urls inside url till the end."""
        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language':
            'en-US,en;q=0.8,ru;q=0.6',
            'upgrade-insecure-requests': '1',
            'user-agent':
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'accept':
                'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'cookie': 'cookie: _ym_uid=1484309026450282985; showNewFeatures=7; showNewFeaturesMainPage=4; left_filter_test=1;'

        }
        resp = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        ads = soup.find_all('a', {'class': 'address'}, href=True)
        unique_urls = []
        for ad in ads:
            if ad['href'] not in unique_urls:
                unique_urls.append(ad['href'])
        if len(unique_urls) > 0:
            self.start_urls.extend(unique_urls)
            next_page_url = '{}&page={}'.format(self.search_url, self.page_counter) 
            self.page_counter += 1
            self.find_urls(next_page_url)


    def start_requests(self):
        """Use search url and get the list of ads urls."""
        self.find_urls(self.search_url)
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

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
