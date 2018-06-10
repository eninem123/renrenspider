# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from Test.settings import USER_AGENT_LIST
import random

class UserAgentMiddleware:
    def process_request(self, request,spider):

        user_agent = random.choice(USER_AGENT_LIST)
        request.headers["User-Agent"] = user_agent
        # print(request.headers["User-Agent"])


class ProxyMiddleware:
    def process_request(self,request,spider):
        proxy = "maozhaojun:ntkn0npx@114.67.142.128:16816"
        request.meta["proxy"] = "http://" + proxy