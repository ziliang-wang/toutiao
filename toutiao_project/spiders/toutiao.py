import scrapy
from scrapy_splash import SplashRequest
from toutiao_project.items import ToutiaoProjectItem


class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    lua_code = """
        function main(splash, args)
            splash.resource_timeout = 0
            js1 = 'window.scrollTo(0, document.body.scrollHeight/2)'
            js2 = 'window.scrollTo(0, document.body.scrollHeight)'
            splash:go(args.url)
            splash:wait(args.wait)
            splash:runjs(js1)
            for i=0,8 do
                splash:wait(args.wait)
                splash:runjs(js2)
            end
            return splash:html()
        end
    """
    url = 'https://www.toutiao.com/ch/news_hot/'

    def start_requests(self):
        yield SplashRequest(self.url,
                            callback=self.parse_toutiao,
                            endpoint='execute',
                            args={'lua_source': self.lua_code,
                                  'wait': 3,
                                  'images': 0})

    def parse_toutiao(self, response):
        item = ToutiaoProjectItem()
        lis = response.xpath('//div[@class="wcommonFeed"]//li')
        for li in lis:
            try:
                item['title'] = li.xpath('.//a[@class="link title"]/text()'
                                             ).extract_first().strip()
                item['source'] = li.xpath('.//a[@class="lbtn source"]/text()'
                                              ).extract_first().lstrip().rstrip('\xa0⋅')
                item['comment'] = li.xpath('.//a[@class="lbtn comment"]/text()'
                                               ).extract_first().lstrip().rstrip('\xa0⋅')
            except:
                pass
            else:
                yield item


