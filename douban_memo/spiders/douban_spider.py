# -*- coding: utf-8 -*-
import scrapy
from douban_memo.items import DoubanMemoItem
from scrapy.http import Request, FormRequest


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]

    start_urls = [
        "http://www.douban.com",
    ]

    def start_requests(self):
        return [Request('https://www.douban.com/accounts/login',
                        meta={'cookiejar': 1},
                        callback=self.parse_login)]

    def parse_login(self, response):
        print 'Preparing login'
        meta = {'cookiejar': response.meta['cookiejar']}
        formdata = {'form_email': 'zztczcx@163.com',
                    'form_password': '1qw34rzcxdouban'}

        return [FormRequest.from_response(response, meta=meta,
                                          formdata=formdata,
                                          callback=self.after_login,
                                          dont_filter=True)]

    def after_login(self, response):
        print 'after login'
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_page(self, response):
        print 'parse'
