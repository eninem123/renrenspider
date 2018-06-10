# -*- coding: utf-8 -*-
import scrapy


class RenrenLoginSpider(scrapy.Spider):
    name = 'renren_login'
    allowed_domains = ['renren.com']
    #start_urls = ['http://renren.com/']


    def start_requests(self):
        login_url = "http://www.renren.com/PLogin.do"
        data = {
            "email" : "2442972114@qq.com",
            "password" : "zxc123456"
        }
        # data = {
        #     "email": "mr_mao_hacker@163.com",
        #     "password": "alarmchime"
        # }
        # 发送post请求，formdata表示发送的表单数据
        # 如果模拟登录成功，Scrapy会自动记录登录状态的Cookies，并传递给后面的请求
        yield scrapy.FormRequest(url = login_url, formdata = data, callback = self.parse)

    @staticmethod
    def get_link_list():
        """
        、   自定义函数，处理额外工作
        """
        # link_list = [
        #     'http://www.renren.com/315391154/profile',
        # 'http://www.renren.com/354189039/profile'
        # ]
        link_list = [
            'http://www.renren.com/327550029/profile',
            'http://www.renren.com/410043129/profile'
        ]
        # 返回给调用的地方，而不是给引擎
        return link_list

    def parse(self, response):
        # 调用自定义方法，处理额外工作
        link_list = self.get_link_list()

        for link in link_list:
            # 因为模拟登录成功，Scrapy已经记录Cookies，所以可以直接发送其他页面的get请求
            yield scrapy.Request(link, callback = self.after_login)

    def after_login(self, response):
        filename = response.xpath("//head/title/text()").extract_first()

        with open(filename + ".html", "w") as f:
            f.write(response.body.decode())
