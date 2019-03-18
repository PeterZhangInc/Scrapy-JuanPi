import scrapy
import json


class GoodsDetailSpider(scrapy.Spider):
    name = 'goods_detail_spider'

    def start_requests(self):
        with open("goods_list.json", "r", encoding="utf-8") as f:
            goods = json.loads(f.read())
            f.seek(0)

        for good in goods:
            yield scrapy.Request(url=good['url'], callback=self.parse, meta=good)

    def parse(self, response):
        yield {
            'id': response.meta['id'],
            'price': response.css('span.js-cprice::text')[0].extract(),
            'org_price': response.css('span.js-oprice::text')[0].extract(),
            'img': response.css('div.deal-pic div.pic img::attr(src)')[0].extract(),
            'desc': response.css('div.tm-goodsinfo')[0].extract()
        }
