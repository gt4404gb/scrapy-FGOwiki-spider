
import scrapy
import re
from ..items import TutorialItem #..代表上一级
from scrapy_splash import SplashRequest


class DmozSpider(scrapy.Spider):
    #定义爬虫名
    name = "demo"
     #搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页
    allowed_domains = [""]
    #用for构造url
    start_urls = []
    for i in range(865):
        start_urls.append('https://fgowiki.com/guide/equipdetail/%s'%i)
    print(start_urls)
    # 设置爬虫的请求头，防止爬取失败
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    }
    # 定义主页面爬取规则，有其他链接则继续深挖
    #rules = (Rule(LinkExtractor(allow=('.+?\.html')), follow=True),

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url
                                ,self.parse
                                ,args={'wait':'0.5'}
                                )
        pass

#该函数名不能改变，因为Scrapy源码中默认callback函数的函数名就是parse
    def parse(self, response):
        item = TutorialItem()
        image_style = response.xpath('//li[@class="swiper-slide eq Card"]/@style').extract() #返回一个list，但这个list里只有一条
        item['image_urls'] = re.search(r'http.*?jpg',image_style[0]).group()
        item['name'] = response.xpath('//div[@class="textsmall NAME_CN"]//text()').extract_first()
        item['author'] = response.xpath('//div[@class="textsmall ILLUST"]//text()').extract_first()
        yield item
        print("返回item成功")
