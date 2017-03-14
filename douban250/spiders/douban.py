# -*- coding: utf-8 -*-
# @Time     : 2017/3/14 15:24
# @Author   : daxiahy


from scrapy import Request
from scrapy.spiders import Spider
from douban250.items import Douban250Item
from bs4 import BeautifulSoup


class DoubanMovieTop250Spider(Spider):
    name = 'douban250'

    start_urls = (
        'https://movie.douban.com/top250',
    )

    def parse(self, response):
        item = Douban250Item()
        soup=BeautifulSoup(response.body, 'html.parser', from_encoding='utf-8')
        movies = soup.select('.info')
        for movie in movies:
            title = movie.a.text.strip()
            movieInfo = movie.p.text
            star = movie.select('.rating_num')[0].text
            quote = movie.select('.inq')
            url = movie.a.get('href')
            if quote:
                quote=quote[0].text
            else:
                quote='no quote'

            item['title']=title
            item['movieInfo']=movieInfo
            item['star']=star
            item['quote']=quote
            item['url']=url

            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url)