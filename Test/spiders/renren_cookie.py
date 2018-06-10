# -*- coding: utf-8 -*-
import scrapy


class RenrenCookiesSpider(scrapy.Spider):
    name = 'renren_cookies'
    allowed_domains = ['renren.com']
    start_urls = [
        'http://www.renren.com/315391154/profile',
        'http://www.renren.com/354189039/profile']



    cookies = {"anonymid": "jhmrgevc8i41ge",
               "_r01_": "1",
               "ln_uact": "2442972114@qq.com",
               "ln_hurl": "http://hdn.xnimg.cn/photos/hdn421/20131205/1700/h_main_poze_fc390000a5c4111a.jpg",
               "_ga": "GA1.2.1149263056.1527322161",
               "depovince": "GW",
               "JSESSIONID": "abckZNk__PIZ67UR_mFpw",
               "ick_login": "41f9400f-301b-46a2-9ef2-3e4e79e92f56",
               "jebe_key": "7ba5938a-f74b-480f-ba00-f76d7768cfe4%7Ce93df0aa8b9384ad4e8cac1ebca30038%7C1527303021269%7C1%7C1528458109385",
               "ick": "2ca8684b-787e-4178-a084-a7f8fb2f1ddb",
               "__utma": "151146938.1149263056.1527322161.1528458214.1528458214.1",
               "__utmc": "151146938",
               "__utmz": "151146938.1528458214.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/",
               "first_login_flag": "1",
               "loginfrom": "syshome",
               "ch_id": "10016",
               "wp_fold": "0",
               "wp": "0",
               "jebecookies": "f1a3bc22-a300-4dc7-bdff-b9a25242ea3f|||||",
               "_de": "9A485391C8BE343441F6ED13F90649A76DEBB8C2103DE356",
               "p": "60acdc304ce4398294d08b6623ac32aa3",
               "t": "434d75a4048607381b121e6153a50a203",
               "societyguester": "434d75a4048607381b121e6153a50a203",
               "id": "430332643",
               "xnsid": "2099c9b1"}


    def start_requests(self):
        # 发送start_urls的请求，并附带登录状态的Cookies
        for url in self.start_urls:
            yield scrapy.Request(url,cookies = self.cookies, dont_filter=True)

    def parse(self, response):
        filename = response.xpath("//head/title/text()").extract_first()

        with open(filename + ".html", "w") as f:
            f.write(response.body.decode())
