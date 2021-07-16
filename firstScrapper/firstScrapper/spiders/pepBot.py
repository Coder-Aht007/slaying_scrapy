import scrapy


class PepbotSpider(scrapy.Spider):
    name = 'pepBot'
    allowed_domains = ['https://www.python.org/dev/peps/pep-0008/#id16']
    start_urls = ['http://https://www.python.org/dev/peps/pep-0008/#id16/']

    def parse(self, response):
        pass
