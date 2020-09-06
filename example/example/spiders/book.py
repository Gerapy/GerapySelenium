# -*- coding: utf-8 -*-
import re
import scrapy
from example.items import BookItem
from gerapy_selenium import SeleniumRequest
import logging

logger = logging.getLogger(__name__)


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['dynamic5.scrape.center']
    base_url = 'https://dynamic5.scrape.center'
    
    def start_requests(self):
        """
        first page
        :return:
        """
        start_url = f'{self.base_url}/page/1'
        logger.info('crawling %s', start_url)
        yield SeleniumRequest(start_url, callback=self.parse_index, wait_for='.item .name')
    
    def parse_index(self, response):
        """
        extract books and get next page
        :param response:
        :return:
        """
        items = response.css('.item')
        for item in items:
            href = item.css('.top a::attr(href)').extract_first()
            detail_url = response.urljoin(href)
            yield SeleniumRequest(detail_url, callback=self.parse_detail, wait_for='.item .name', priority=2)
        
        # next page
        match = re.search(r'page/(\d+)', response.url)
        if not match: return
        page = int(match.group(1)) + 1
        next_url = f'{self.base_url}/page/{page}'
        yield SeleniumRequest(next_url, callback=self.parse_index, wait_for='.item .name')
    
    def parse_detail(self, response):
        """
        process detail info of book
        :param response:
        :return:
        """
        name = response.css('.name::text').extract_first()
        tags = response.css('.tags button span::text').extract()
        score = response.css('.score::text').extract_first()
        tags = [tag.strip() for tag in tags] if tags else []
        score = score.strip() if score else None
        item = BookItem(name=name, tags=tags, score=score)
        yield item
