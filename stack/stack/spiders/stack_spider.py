import pdb
from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
            #"http://stackoverflow.com/questions?pagesize=50&sort=newest", 
            #"http://stackoverflow.com/questions",  
            "http://www.sina.com.cn"]

    def parse(self, response):
        content = Selector(response)
        print content
        #questions = Selector(response).xpath('//dev[@class="summary"]/h3')
        questions = Selector(response).xpath('//*[@id="question-summary-30051189"]/div[2]')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                    'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                    'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item

