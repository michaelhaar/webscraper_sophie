# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CondoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    room_count = scrapy.Field()
    postal_code = scrapy.Field()
    district = scrapy.Field()
    discovery_date = scrapy.Field()
    edit_date = scrapy.Field()
    description = scrapy.Field()
    address = scrapy.Field()
    willhaben_code = scrapy.Field()
    commission_fee = scrapy.Field()
    price_per_m2 = scrapy.Field()

    DEFAULT_VALUE_STRING = ''
    DEFAULT_VALUE_INT = 0
    DEFAULT_VAULE_BOOL = False

    def set_default_values(self):
        # init fields if needed
        # no init value needed for self['url'] and self['discovery_date']
        self['title'] = self.DEFAULT_VALUE_STRING
        self['price'] = self.DEFAULT_VALUE_INT
        self['size'] = self.DEFAULT_VALUE_INT
        self['room_count'] = self.DEFAULT_VALUE_INT
        self['postal_code'] = self.DEFAULT_VALUE_STRING
        self['district'] = self.DEFAULT_VALUE_STRING
        self['edit_date'] = self.DEFAULT_VALUE_STRING
        self['description'] = self.DEFAULT_VALUE_STRING
        self['address'] = self.DEFAULT_VALUE_STRING
        self['willhaben_code'] = self.DEFAULT_VALUE_STRING
        self['commission_fee'] = self.DEFAULT_VALUE_STRING
        self['price_per_m2'] = self.DEFAULT_VALUE_INT

    def calc_price_per_m2(self):
        """ Calculate the price per square meter. """
        if self['size']:
            self['price_per_m2'] = self['price'] / self['size']
