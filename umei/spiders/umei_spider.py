# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import UmeiItem

class UmeiSpiderSpider(CrawlSpider):
    name = 'umei_spider'
    allowed_domains = ['umei.cc']
    start_urls = ['http://www.umei.cc/bizhitupian/']
    rules = (
        Rule(LinkExtractor(allow=r'http://www.umei.cc/bizhitupian/[a-z]+\/$'), follow=True),
        Rule(LinkExtractor(allow=r'http://www.umei.cc/bizhitupian/.+.htm$'), callback='parse_item', follow=False),
    )


    def parse_item(self, response):
        category = response.xpath("//span[@class='column']/a/text()").get()
        pic_url = response.xpath("//p[@align='center']//img/@src").get()
        item = UmeiItem()
        item['category'] = category
        if pic_url:
            item['image_urls'] = [pic_url]

        yield item