# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class ExchangeCrawlerPipeline:
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):

        # Create/Connect to database
        self.con = sqlite3.connect('demo.db')

        # Create cursor, used to execute commands
        self.cur = self.con.cursor()
        print("=================================")
        print("Connected!")
        print("=================================")
        # Create exchanges table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Exchanges(
            usd REAL,
            euro REAL,
            scrap_date TEXT,
            valid_date TEXT
        );
        """)

    def process_item(self, item, spider):
        print("=================================")
        print(item)
        print("=================================")
        print(float(item.get('usd')[0].replace(",", ".")),)
        print(float(item.get('euro')[0].replace(",", ".")),)
        print(str(item.get('scrap_date')[0]))
        print(str(item.get('valid_date')[0]))
        # Define insert statement
        # INSERT INTO Exchanges (usd, euro, scrap_date, valid_date) VALUES (?, ?, ?, ?);
        self.cur.execute("""
            INSERT INTO Exchanges
            (usd, euro, scrap_date, valid_date)
            VALUES(?, ?, ?, ?);
        """,
                         (
                             float(item.get('usd')[0].replace(",", ".")),
                             float(item.get('euro')[0].replace(",", ".")),
                             str(item.get('scrap_date')[0]),
                             str(item.get('valid_date')[0])
                         ))

        # Execute insert of data into database
        self.con.commit()
        return item
