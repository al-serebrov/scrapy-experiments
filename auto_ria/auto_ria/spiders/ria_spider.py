import scrapy
import requests
import re
import csv
from collections import OrderedDict
from bs4 import BeautifulSoup

class RiaSpider(scrapy.Spider):
    name = "auto_ria"
    start_urls = []
    page_counter = 1

    def __init__(self, url=None, f=None, *args, **kwargs):
        super(RiaSpider, self).__init__(*args, **kwargs)
        self.search_url = url
        self.input_file = f

    def handle_params(self, url, filename):
        if filename is not None:
            self.logger.info('Parsing csv file')
            self.parse_csv(filename)
        elif url is not None:
            self.analyse_url(url)
        else:
            self.logger.critical('''You need to provide either url or csv file with urls(s)''')

    def parse_csv(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.analyse_url(row[0])

    def analyse_url(self, url):
        self.logger.debug('Analysing url')
        if url is not None:
            search_regex = re.compile(r'https://auto.ria.com/search.*')
            single_regex = re.compile(r'https://auto.ria.com/auto.*')
            if re.search(search_regex, url) is not None:
                # means that we have an url to the search
                self.logger.debug('search url match')
                self.find_urls(url)
            elif re.search(single_regex, url) is not None:
                # url to a single item
                self.logger.debug('single url match')
                self.append_url(url)
            else:
                self.logger.debug('no url found')

    def append_url(self, url):
        self.start_urls.append(url)

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
        self.handle_params(self.search_url, self.input_file)
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        params = [
            ('Link', response.url),
            ('Brand',
                response.css('span[itemprop="brand"]::text').extract_first()),
            ('Model',
                response.css('span[itemprop="name"]::text').extract_first()),
            ('Name',
                response.css('dt.user-name strong::text').extract_first()),
            ('Phone',
                response.css('span.mhide::attr(data-phone-number)').extract_first()),
            ('Price', response.css('span.price::text').extract_first()),
            ('City',
                response.css('span[title="Город продавца"]::text').extract_first()),
            ('Mileage', response.css('div.run strong::text').extract_first()),
            ('Year', response.css('span.year::text').extract_first())
        ]
        yield OrderedDict(params)
