# -*- coding: utf-8 -*-
import scrapy
import logging

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.body)
        # print("正在测试代码...")
        logging.info("正在测试代码...")
        logging.log(logging.WARNING, "this is warning")
