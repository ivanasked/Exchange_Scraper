import scrapy
from exchange_crawler.items import ExchangeCrawlerItem
from datetime import datetime
from scrapy.loader import ItemLoader


class BcvSpider(scrapy.Spider):
    name = 'bcv'

    def start_requests(self):
        url = 'https://www.bcv.org.ve/'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        l = ItemLoader(item=ExchangeCrawlerItem(), response=response)
        l.add_xpath(
            'usd', '//*[@id="dolar"]//div[@class="col-sm-6 col-xs-6 centrado"]/strong/text()')
        l.add_xpath(
            'euro', '//*[@id="euro"]//div[@class="col-sm-6 col-xs-6 centrado"]/strong/text()')
        l.add_xpath(
            'valid_date', '/html/body/div[4]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[2]/div/div[8]/span/text()')
        l.add_value('scrap_date', datetime.today().strftime(
            '%Y-%m-%d %H:%M:%S')) 
        return l.load_item()