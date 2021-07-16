import scrapy


class MobilebotSpider(scrapy.Spider):
    name = 'mobileBot'
    allowed_domains = ['https://www.whatmobile.com.pk']
    start_urls = ['https://www.whatmobile.com.pk/']

    def parse(self, response):
        mobileName = response.xpath("//h4/a[contains(@class, 'BiggerText')]/@title").extract()
        mobilePrice = response.xpath("//li/span[contains(@class, 'PriceFont')]/text()").extract()

        for item in zip(mobileName, mobilePrice):
            yield {
                "name" : item[0],
                "price" : item[1],
            }
