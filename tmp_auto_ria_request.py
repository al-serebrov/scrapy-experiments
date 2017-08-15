import requests
import urllib

url_start = 'https://auto.ria.com/search/?category_id=1&marka_id=62&model_id=1560&state%5B0%5D=0&s_yers%5B0%5D=0&po_yers%5B0%5D=2007&price_ot=&price_do=&currency=1&scrollToAuto=20253935&page=0'

url = 'https://auto.ria.com/search/'
s = requests.Session()
s.get('https://auto.ria.com')
cookies = requests.utils.dict_from_cookiejar(s.cookies)
print(cookies)
params = urllib.parse.parse_qs(urllib.parse.urlparse(url_start).query)
s.headers.update = ({
    'accept-encoding': 'gzip, deflate, br',
    'accept-language':
    'en-US,en;q=0.8,ru;q=0.6',
    'upgrade-insecure-requests': '1',
    'user-agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#    'showNewFeatures': '7',
#    'showNewFeaturesMainPage':'4',
#    'left_filter_test': '1'
    'cookie': '''test_all_for_auto=1;
    __utma=79960839.979811160.1502713418.1502781681.1502787477.4;
    __utmc=79960839;
    __utmz=79960839.1502713418.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);
    chk=1; _ga=GA1.3.979811160.1502713418; _gid=GA1.3.20933197.1502713421;
    ui=241bec552ae556fa;
    __gads=ID=46cc69da3621d8fd:T=1502713420:S=ALNI_MaNVfpFmBcrQal3Svpv7Pn9xdCsBA;
    showNewFeatures=7; showNewFeaturesMainPage=3;
    view_news_prior_234132_undefined_234141_234149_234145_234029=%7B%22item0%22%3A5%2C%22item1%22%3A4%2C%22item2%22%3A3%2C%22item3%22%3A2%2C%22item4%22%3A1%7D;
    PHPSESSID=y8xn7FyMAYa3RGve6kWsx8vRTZbHKfx8; opros_53_cansel=1;
    left_filter_test=1; showNewNextAdvertisement=10;
    view_news_prior_234132_undefined_234157_234161_234158_234029=%7B%22item0%22%3A5%2C%22item1%22%3A4%2C%22item2%22%3A3%2C%22item3%22%3A2%2C%22item4%22%3A1%7D;
    __utmb=79960839.12.8.1502804033676; __utmt=1; __utmt_b=1'''

})

resp = s.get(url=url, params=params)
print(resp, resp.url, resp.headers)

with open('tmp.html', 'w') as fname:
    print(resp.text, file=fname)
