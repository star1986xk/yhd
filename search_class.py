import requests
from lxml import etree
import re
from settings import *
import copy
import time
import json
from db_class import db_class
from PyQt5.QtCore import QThread
from threading import Thread
from PyQt5.QtCore import pyqtSignal


# 搜索类
class search_class(QThread):
    sig_one_end = pyqtSignal(str)
    sig_end = pyqtSignal(str)

    def __init__(self, url_class_list=None, page_count=None, thread_count=None):
        '''
        初始化
        :param url_class: 类型url
        :param page_count: 查询页数
        :param thread_count: 线程数
        '''
        super(search_class, self).__init__()
        self.flag = True
        self.url_class_list = url_class_list
        self.page_count = int(page_count) + 1
        self.thread_count = int(thread_count)
        self.uid = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def requestGET(self, url, headers):
        '''
        get请求
        :param url: url
        :return: 返回text或none
        '''
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            return None

    def parser_index(self, url):
        '''
        解析索引页
        :param url: 索引页url
        :return:
        '''
        try:
            db = db_class()
            db.open()
            # 请求索引页
            text = self.requestGET(url, headers)
            if text:
                html = etree.HTML(text)
                skuIds = html.xpath('//em[@class="num"]/@id')
                skuIds = [id.split('_')[-1] for id in skuIds]
                moneys = html.xpath('//em[@class="num"]/text()')
                moneys = [m.strip() for m in moneys if m.strip()]
                titles = html.xpath('//a[@class="mainTitle"]/@title')
                shops = html.xpath('//span[@class="shop_text"]/text()')
                for skuId, money, title, shop in zip(skuIds, moneys, titles, shops):
                    obj = copy.deepcopy(item_obj)
                    obj['uid'] = self.uid
                    obj['skuId'] = skuId
                    obj['title'] = title
                    obj['money'] = money
                    obj['shop'] = shop
                    obj['url'] = url_item.format(skuId)
                    obj = self.parser_item(obj)
                    if obj:
                        if db.insert_many(table_name, [obj]):
                            self.sig_one_end.emit(
                                '抓取成功：' + obj['title'] + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        except Exception as e:
            print(e)
        finally:
            db.close()

    def parser_item(self, obj):
        '''
        解析商品详情页
        :param url:详情页url
        :return:
        '''
        # 请求详情页
        try:
            text = self.requestGET(obj['url'], headers=headers)
            if text:
                html = etree.HTML(text)
                class_all = html.xpath('//div[@class="detail_wrap"]//div/a/em/text()')
                obj['class1'] = class_all[0]
                obj['class2'] = class_all[1]
                obj['class3'] = class_all[2]
            # 请求评分接口
            headers['referer'] = obj['url']
            text = self.requestGET(url_score.format(obj['skuId']), headers=headers)
            result = re.search('\((.*?)\)', text)
            obj['sales'] = json.loads(result[1])['data']['result']['commentSummaries'][0]['commentCount']
            obj['averageScore'] = json.loads(result[1])['data']['result']['commentSummaries'][0]['averageScore']
            obj['goodCount'] = json.loads(result[1])['data']['result']['commentSummaries'][0]['goodCount']
            obj['generalCount'] = json.loads(result[1])['data']['result']['commentSummaries'][0]['generalCount']
            obj['poorCount'] = json.loads(result[1])['data']['result']['commentSummaries'][0]['poorCount']
            return obj
        except Exception as e:
            return None

    def thread_pool(self):
        '''
        线程池,多线程解析索引页
        :return:
        '''
        try:
            for url_class in self.url_class_list:
                for i in range(1, self.page_count, self.thread_count):
                    if self.flag:
                        self.result = []
                        self.task_list = [Thread(target=self.parser_index, args=(url_class + url_index.format(n),)) for
                                          n in range(i, i + self.thread_count)]
                        [task.start() for task in self.task_list]
                        [task.join() for task in self.task_list]
                        time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            self.sig_end.emit('运行结束！ ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 执行函数
    def run(self):
        self.thread_pool()
