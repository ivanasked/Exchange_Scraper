# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass
import scrapy

class ExchangeCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    usd = scrapy.Field()
    euro = scrapy.Field()
    scrap_date = scrapy.Field()
    valid_date = scrapy.Field()    
