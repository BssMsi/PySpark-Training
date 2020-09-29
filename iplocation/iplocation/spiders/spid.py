from scrapy import Request
from scrapy.spiders import CrawlSpider
import pandas as pd
#from tqdm import tqdm
import re
import json
import os

class IPLocation(CrawlSpider):
    name = "IPLocation"
    #allowed_domains = ['ipinfo.io']
    
    locations = open('IPLocation1.json', 'a')
    count_success = 0

    mylog = ""
    def start_requests(self):
        df = pd.read_csv('all_ips.csv', header=None, index_col=0, names=['IP'])
        for url in map(lambda ip: f"https://geolocation-db.com/json/{ip}", df.IP):
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        self.locations.write(str(response.text).replace("\n", "")+"\n")
        self.count_success += 1

    def close(self, spider):
        self.locations.close()
        print(f"Success: {self.count_success}")
