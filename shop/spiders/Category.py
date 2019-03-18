import scrapy


class CategorySpider(scrapy.Spider):
    name = 'category_spider'

    def start_requests(self):
        urls = [
            'https://www.juanpi.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.banner_l dd'):
            yield {
                'text': quote.css('a::text')[1].extract().strip(),
                'url': 'https:' + quote.css('a::attr(href)')[0].extract()
            }
