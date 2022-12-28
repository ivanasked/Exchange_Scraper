# Exchange Crawler

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```python
import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime
import json


class PythonListingSpider(scrapy.Spider):
    name = 'pythonlistingssspider'

    start_urls = ['https://www.bcv.org.ve/', ]
    found_listings = []

    def parse(self, response):
        usd = response.xpath(
            '//*[@id="dolar"]//div[@class="col-sm-6 col-xs-6 centrado"]/strong/text()').get()
        euro = response.xpath(
            '//*[@id="euro"]//div[@class="col-sm-6 col-xs-6 centrado"]/strong/text()').get()
        valid_date = response.xpath(
            '/html/body/div[4]/div/div[2]/div/div[1]/div[1]/section[1]/div/div[2]/div/div[8]/span/text()').get()
        exchange_rate = {
            "usd": float(usd.replace(",",".")), 
            "euro": float(euro.replace(",",".")),
            "scrap_date": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            "valid_date": valid_date.split(",")[1] 
        }
        
        self.found_listings.append(exchange_rate)


if __name__ == "__main__":
    process = CrawlerProcess({'LOG_LEVEL': 'ERROR'})
    process.crawl(PythonListingSpider)
    spider = next(iter(process.crawlers)).spider
    process.start()

    print(json.dumps(PythonListingSpider.found_listings, indent=4))

```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
