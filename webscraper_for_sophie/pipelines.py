# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from webscraper_for_sophie.database_manager import DatabaseManager


class WebscraperForSophiePipeline:

    def open_spider(self, spider):
        """ This method is called when the spider is opened. """
        self.db_manager = DatabaseManager()
        self.db_manager.connect()
        self.db_manager.prep_table()

    def close_spider(self, spider):
        """ This method is called when the spider is closed. """
        self.db_manager.close()

    def process_item(self, item, spider):
        """ This method is called for every item pipeline component. """
        self.db_manager.store_item(item)
        return item
