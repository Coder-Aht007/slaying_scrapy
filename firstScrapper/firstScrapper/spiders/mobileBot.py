import scrapy


class MobilebotSpider(scrapy.Spider):
    name = 'mobileBot'
    allowed_domains = ['https://www.whatmobile.com.pk']
    start_urls = ['http://https://www.whatmobile.com.pk/']

    def parse(self, response):
        pass
