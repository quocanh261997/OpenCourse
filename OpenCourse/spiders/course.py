# -*- coding: utf-8 -*-
import scrapy
import logging

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
        nextLink = 'https://bannerweb.miamioh.edu/pls/banweb/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu'
        yield scrapy.FormRequest(nextLink, callback=self.nextPage)

    def nextPage(self, response):
        yield {
            'author': 'Quanh'
        }



    
