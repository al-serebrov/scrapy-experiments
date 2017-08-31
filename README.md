# scrapy-auto-ria
This module is intended to export classifieds information from https://auto.ria.com to csv file.
Could be convenient if you're planning to call car owners, to keep track of convesations, their statuses and so on.

## Installation

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

There are a couple usage scenarios, but each time you run a script it replaces the output file (`items.csv`), keep it in mind.

### Passing an URL as a command line parameter

```
$ scrapy crawl auto_ria -a url="https://auto.ria.com/search/?marka_id[0]=0&model_id[0]=0&s_yers[0]=2016&po_yers[0]=2017&brandOrigin[0]=276&brandOrigin[1]=356&brandOrigin[2]=380&price_ot=10000&price_do=11000&currency=1&abroad=2&custom=1&fuelRatesType=city&engineVolumeFrom=&engineVolumeTo=&power_name=1&countpage=20"
```
Here you can pass either search URL or sigle classified URL, the script will handle both types

### Passing a .csv file name as a command line parameter

```
$ scrapy crawl auto_ria -a f="my_file_with_links.csv"
```

The script expects links (no matter to the search results of single car) to be in the first column of csv file.
Everything except urls is ignored.
