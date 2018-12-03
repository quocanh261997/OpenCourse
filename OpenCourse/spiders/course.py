# -*- coding: utf-8 -*-
import scrapy


class CourseSpider(scrapy.Spider):
    name = 'course'
    start_urls = ['https://bannerweb.miamioh.edu/pls/banweb/twbkwbis.P_WWWLogin']

    def parse(self, response):
        data = {
            'sid': 'nguyenq2',
            'PIN': '*BiQuanh2606'
        }       
        return scrapy.FormRequest.from_response(response, formdata=data, callback=self.after_login)
    
    def after_login(self, response):
        yield {
            'author': 'Quoc Anh',
            'class': 'CSE262'
        }



    
