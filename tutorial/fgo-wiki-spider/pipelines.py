# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class TutorialPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print("获取URL")
        yield scrapy.Request(item['image_urls'], meta={'item': item, 'index': item['image_urls']})


    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # 通过上面的meta传递过来item
        image_name = "礼装-" + item['name'] + "." + request.url.split('/')[-1].split('.')[-1]
        down_file_name = u'/{0}/{1}'.format(item['author'], image_name)
        return down_file_name
