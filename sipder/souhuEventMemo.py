# -*- coding: UTF-8 -*-
"""
爬去搜狐证券重大事项备忘重大事件备忘录
"""
from lxml import etree
import requests
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    htmltree = selector.xpath('//tr[starts-with(@id,"tr")]')
    item = {}
    for each in htmltree:
        time = each.xpath('td[@class="e1"]/text()')
        time = ''.join(time).replace('\t', '').replace('\n', '').replace('\r', '')
        content = each.xpath('td[@class="e2"]/text()')
        content = ''.join(content).replace('\t', '').replace('\n', '')
        event = each.xpath('td[@class="e3"]/text()')
        event = ''.join(event).replace('\t', '').replace('\n', '')
        union = time + '\t' + content + '\t' + event + '\t\n'
        print union
        f.write(str(union))


# def towrite(contentdict):
#     f.writelines(u'公告日期:' + contentdict['time'] + '\n')
#     f.writelines(u'备忘事项:' + contentdict['content']+ '\n')
#     f.writelines(u'事件类型:' + contentdict['event'] + '\n\n')


if __name__ == '__main__':
    url = 'http://q.stock.sohu.com/cn/300059/bw.shtml?qq-pf-to=pcqq.c2c'
    f = open('union.txt', 'a')
    spider(url)

