# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CondoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field(default='')
    title = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    postal_code = scrapy.Field()
    district = scrapy.Field()
    discovery_date = scrapy.Field()
    edit_date = scrapy.Field()
    parking = scrapy.Field()
    garage = scrapy.Field()
    carport = scrapy.Field()
    description = scrapy.Field()
    contact = scrapy.Field()
    address = scrapy.Field()
    ad_body = scrapy.Field()
    ad_info_desc = scrapy.Field()
    ad_info_values = scrapy.Field()
    willhaben_code = scrapy.Field()
    commission_fee = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
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
        self['postal_code'] = self.DEFAULT_VALUE_STRING
        self['district'] = self.DEFAULT_VALUE_STRING
        self['edit_date'] = self.DEFAULT_VALUE_STRING
        self['parking'] = self.DEFAULT_VAULE_BOOL
        self['garage'] = self.DEFAULT_VAULE_BOOL
        self['carport'] = self.DEFAULT_VAULE_BOOL
        self['description'] = self.DEFAULT_VALUE_STRING
        self['contact'] = self.DEFAULT_VALUE_STRING
        self['address'] = self.DEFAULT_VALUE_STRING
        self['ad_body'] = self.DEFAULT_VALUE_STRING
        self['ad_info_desc'] = self.DEFAULT_VALUE_STRING
        self['ad_info_values'] = self.DEFAULT_VALUE_STRING
        self['willhaben_code'] = self.DEFAULT_VALUE_STRING
        self['commission_fee'] = self.DEFAULT_VALUE_STRING
        self['image_urls'] = self.DEFAULT_VALUE_STRING
        self['image_paths'] = self.DEFAULT_VALUE_STRING
        self['price_per_m2'] = self.DEFAULT_VALUE_INT
