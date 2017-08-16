import requests
from bs4 import BeautifulSoup

url_start = \
'https://auto.ria.com/search/?marka_id[0]=62&model_id[0]=1560&s_yers[0]=0&po_yers[0]=0&marka_id[1]=62&model_id[1]=18484&s_yers[1]=0&po_yers[1]=0&price_do=7000&currency=1&abroad=2&custom=1&type[1]=2&fuelRatesType=city&engineVolumeFrom=&engineVolumeTo=&power_name=1&countpage=10'

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

resp = requests.get(url=url_start, headers=headers)

with open('tmp.html', 'w') as fname:
    fname.write(resp.text)

soup = BeautifulSoup(resp.text, 'html.parser')
ads = soup.find_all('span', {'class': 'blue bold'})
print(len(ads))
for ad in ads:
    print(ad)

