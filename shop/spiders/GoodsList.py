import scrapy
import json


class GoodsListSpider(scrapy.Spider):
    name = 'goods_list_spider'

    def start_requests(self):
        with open("category.json", "r", encoding="utf-8") as f:
            urls = json.loads(f.read())
            f.seek(0)

        for cate in urls:
            yield scrapy.Request(url=cate['url'], callback=self.parse, meta=cate)

    def parse(self, response):

        for item in response.css('ul.goods-list li'):
            yield {
                'id': item.css('::attr(id)')[0].extract(),
                'title': item.css('h3.good-title a::text')[0].extract(),
                'url': 'https:' + item.css('div.pic-img a::attr(href)')[0].extract(),
                'type': response.meta['text'],
                'thumb': item.css('div.pic-img img::attr(d-src)')[0].extract()
            }
        """
        next_page = "https://www.juanpi.com" + response.css('a.pg-next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        """

