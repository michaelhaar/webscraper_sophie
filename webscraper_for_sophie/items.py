# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
import logging
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

    MIN_PRICE = 1000
    MAX_PRICE = 1500000
    MIN_SIZE = 10
    MAX_SIZE = 250

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

    def parse_price(self, price_text):
        """ Parses the price from the input text.

        Args:
            price_text (string): something like "€ 99.750"
        """
        cleaned_price_text = price_text.replace('.', '')
        match = re.search(r'\d+', cleaned_price_text)  # search for numbers
        if match:
            price_string = match[0]  # get entire match
            try:
                price_int = int(price_string)   # convert to int
            except ValueError:
                logging.error("Could not convert price to int at page " +
                              self['url'])
            else:
                # realisitic value check
                if price_int > self.MIN_PRICE and price_int < self.MAX_PRICE:
                    self['price'] = price_int
                else:
                    logging.error("Unrealistic price at page " + self['url'])

    def parse_size(self, size_text):
        """ Parses the size from the input text.

        Args:
            size_text (string): something like " 42m²"
        """
        match = re.search(r'\d+', size_text)  # search for numbers
        if match:
            size_string = match[0]  # The entire match
            try:
                size_int = int(size_string)  # convert to int
            except ValueError:
                logging.error("Could not convert size to int at page " +
                              self['url'])
            else:
                # realisitic value check
                if size_int > self.MIN_SIZE and size_int < self.MAX_SIZE:
                    self['size'] = size_int
                else:
                    logging.warning("Unrealistic size at page " + self['url'])
        else:
            logging.error("size parsing failed on page " + self['url'])

    def parse_size_2(self, size_text):
        """ Parses the size from the input text if it contains a keyword

        Keyword is `Nutzfläche`

        Args:
            size_text (string): something like "Nutzfläche: 73m2"
        """
        keyword_match = re.search(r'Nutzfläche', size_text)
        if keyword_match:
            match = re.search(r'\d+', size_text)  # search for numbers
            if match:
                size_string = match[0]  # The entire match
                try:
                    size_int = int(size_string)  # convert to int
                except ValueError:
                    logging.error("Could not convert size to int at page " +
                                  self['url'])
                else:
                    # realisitic value check
                    if size_int > self.MIN_SIZE and size_int < self.MAX_SIZE:
                        self['size'] = size_int
                    else:
                        logging.error(
                            "Unrealistic size at page " + self['url'])
            else:
                logging.error("secondary size parsing failed on page " +
                              self['url'])

    def parse_room_count(self, room_count_text):
        """ Parses the room_count from the input text.

        Args:
            room_count_text (string): something like " 3 Zimmer"
        """
        match = re.search(r'\d', room_count_text)  # search for a single number
        if match:
            room_count_string = match[0]  # The entire match
            try:
                self['room_count'] = int(room_count_string)
            except ValueError:
                logging.error("Could not convert room_count to int at page " +
                              self['url'])
        else:
            logging.warning(
                "room_count parsing failed on page " + self['url'])

    def parse_room_count_2(self, room_count_text):
        """ Parses the room_count from the input text if it contains a keyword

        Keyword is `Zimmer`

        Args:
            room_count_text (string): something like "Zimmer: 3"
        """
        keyword_match = re.search(r'Zimmer', room_count_text)
        if keyword_match:
            match = re.search(r'\d+', room_count_text)  # search for numbers
            if match:
                room_count_string = match[0]  # The entire match
                try:
                    self['room_count'] = int(
                        room_count_string)  # convert to int
                except ValueError:
                    logging.error("Could not convert room_count to int at page "
                                  + self['url'])
            else:
                logging.error("secondary room_count parsing failed on page " +
                              self['url'])
