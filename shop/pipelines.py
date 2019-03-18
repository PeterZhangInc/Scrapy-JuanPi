# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ShopPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='47.93.255.42', port=3306, user='root', passwd='Zhuge123!@#', db='db_ecshop', charset='utf8')
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def process_item(self, item, spider):
        if spider.name == 'category_spider':
            try:
                self.cursor.execute("insert into ecs_category (cat_name) values (%s)", item['text'])
                print("Insert success")
            except Exception as e:
                print("Error", e)
            else:
                self.conn.commit()
            return item

        if spider.name == 'goods_list_spider':
            try:
                self.cursor.execute("insert into ecs_goods (goods_sn, goods_name, goods_name_style, goods_thumb) values (%s, %s, %s, %s)", (item['id'], item['title'], item['type'], item['thumb']))
                print('success')
            except Exception as e:
                print("Error", e)
            else:
                self.conn.commit()
            return item

        if spider.name == 'goods_detail_spider':
            try:
                self.cursor.execute("update ecs_goods set promote_price = %s, shop_price = %s, goods_desc = %s, goods_img = %s, original_img = %s where goods_sn = %s", (item['price'], item['org_price'], item['desc'], item['img'], item['img'], item['id']))
                print('success')
            except Exception as e:
                print("Error", e)
            else:
                self.conn.commit()
            return item