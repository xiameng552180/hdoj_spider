import scrapy
import re
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

UsersConfig = {
    # 代理
    'proxy': '',
    'email': 'placeholder', # placeholder
    'password': 'placeholder', # placeholder
}

class SubmitsSpider(scrapy.Spider):
    name = "submits"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q = 0.8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "acm.hdu.edu.cn",
        "Referer": "http://acm.hdu.edu.cn/status.php",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/65.0.3325.181 Safari/537.36"
    }

    def start_requests(self):
        currentUrl = 'http://acm.hdu.edu.cn/status.php?first=3231790&user=&pid=&lang=&status=#status'
        yield scrapy.Request(url=currentUrl,
                             headers=self.headers,
                             meta={
                                 'currentUrl': currentUrl,
                                 'proxy': UsersConfig['proxy'],
                                 'from': {
                                     'sign': 'else',
                                     'data': {}
                                 }
                             },
                             callback=self.parse)

    def parse(self, response):
        # currUrl = response.meta['currUrl']
        # n_id = int(currUrl.split('first=')[1].split("&user=")[0])
        fixed_table = response.xpath('//div[@id="fixed_table"]/table/tr')
        order_list = ['', 'time', 'judgeStatus', 'problemID', 'executeTime', 'executeMemory', 'codeLength', 'language', 'author']

        item_dict ={}

        for ind in range(1, 9):
            temp_list = []
            for each_cell in range(1, len(fixed_table)):
                each_line = fixed_table[each_cell]
                temp_list.append(each_line.xpath('.//td')[ind].xpath('.//text()').extract())
            item_dict[order_list[ind]] = temp_list
        temp = ''.join(re.findall(r"\d", str(response.xpath('//div[@id="fixed_table"]/p/a[3]/@href').extract())))
        print("**************")
        print(temp)
        if int(temp) == 1:
            temp = ''.join(re.findall(r"\d", str(response.xpath('//div[@id="fixed_table"]/p/a[2]/@href').extract())))
            print(temp)
            currentPage = int(temp) - 1
            item_dict['url_num'] = currentPage
            with open('badpage.txt', 'a') as bb:
                bb.write(str(currentPage))
                bb.write('\n')
            next = currentPage - 15
        else:
            temp = ''.join(re.findall(r"\d", str(response.xpath('//div[@id="fixed_table"]/p/a[3]/@href').extract())))
            currentPage = int(temp) + 15
            item_dict['url_num'] = currentPage
            next = currentPage - 15
        next_page = 'http://acm.hdu.edu.cn/status.php?first=' + str(next) + '&user=&pid=&lang=&status=#status'
        print("**************")

        yield item_dict
        print(next_page)
        yield scrapy.Request(url = next_page,headers = self.headers, callback = self.parse)







