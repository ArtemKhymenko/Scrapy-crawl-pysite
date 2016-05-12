import scrapy
from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pysite.items import PysiteItem


class PysiteSpider(CrawlSpider):
    name = "pycrawler"
    start_urls = ['https://docs.python.org/2/index.html']

    rules = (Rule(LinkExtractor(deny=(), allow=('docs.python.org/2/tutorial/'), restrict_xpaths=('*')), callback='parse_item', follow=True),)

    def parse_item(self, response):
        sel = Selector(response)
        i = PysiteItem()
        pdfs = []
        i['url'] = response.url
        i['title'] = sel.xpath('/html/head/title/text()').extract()
        return i
