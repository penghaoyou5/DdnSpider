# -*- coding: utf-8 -*-
import scrapy
import sys
from DdnSpider.items import DdnspiderItem
from scrapy.selector import Selector
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

class CdnSpider(scrapy.Spider):
    name = "cdn"
    # allowed_domains = ["*"]
    start_urls = (
        'https://www.pinduoduo.com/',
    )

    def parse(self, response):
        filename = "teacher.html"
        open(filename, 'w').write(response.body)
        sel = Selector(response)
        items = []
        # for link in sel.xpath(
        #         "//ul[@class='js-articles l-works']/li[@class='l-work--big']/article[@class='work work--second-created']/h2[@class='work__title']/a/@href").extract():
        #     link = 'http://bcy.net%s' % link
        #     print link

        # print response.body
        # print response.xpath('//a[contains(@href, "image")]/@href').extract()
        # print response.css('a[href*=image]::attr(href)').extract()
        # print response.xpath('//a[contains(@href, "image")]/img/@src').extract()
        # print response.css('a[href*=image] img::attr(src)').extract()
        # print 1111
        # print response.xpath('//img')
        for link in sel.xpath('//img'):
            print link.xpath('/@src').extract()
            # print link['/@href']
            print link

        soup = BeautifulSoup(response.body, "lxml")
        imgs = soup.select('img')
        print imgs
        for ims_div in imgs:
            try:
                src_link = ims_div['src']
                print src_link
            except Exception as e:
                # print e
                pass
        # response.xpath('')
        # for sel in response.xpath('//ul/li/a').re('href="(/question/.*?.html)'):
        #     print sel
        # for each in response.xpath("//div[@class='li_txt']"):
        # extract = response.xpath('//*[@id="mainpic"]/a/img/@src').extract()
        # if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):  # 如果url能够匹配到需要爬取的url，就爬取
        #     items = hxs.xpath('//div[@class="item_list infinite_scroll"]/div')  # 匹配到大的div下的所有小div（每个小div中包含一个图片）
        #
        #     for i in range(len(items)):  # 遍历div个数
        #         src = hxs.xpath(
        #             '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % i).extract()  # 查询所有img标签的src属性，即获取校花图片地址
        #         # name = hxs.xpath(
        #         #     '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()  # 获取span的文本内容，即校花姓名
        #         # school = hxs.xpath(
        #         #     '//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()  # 校花学校
        #
        #
        #         print src
        #         # if src:
        #         #     absoluteSrc = "http://www.xiaohuar.com" + src[
        #         #         0]  # 拼接实际路径,因为.extract()会返回一个list，但是我们是依次取得div，所以是取第0个
        #             # file_name = "%s_%s.jpg" % (school[0], name[0])  # 拼接文件名，学校_姓名
        #             # file_path = os.path.join("F:\\pics", file_name)  # 拼接这个图片的路径，我是放在F盘的pics文件夹下
        #             # urllib.urlretrieve(absoluteSrc, file_path)  # 接收文件路径和需要保存的路径，会自动去文件路径下载并保存到我们指定的本地路径
        #
        #
        #     all_urls = hxs.xpath('//a/@href').extract()  # 提取界面所有的url
        #     for url in all_urls:  # 遍历获得的url，如果满足条件，继续爬取
        #         if url.startswith('http://www.xiaohuar.com/list-1-'):
        #             yield Request(url, callback=self.parse)
        pass
