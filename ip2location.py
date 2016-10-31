# -*- coding:utf-8 -*-
# author:nick
import sys
import urllib2
import json
from PIL import Image
import cStringIO


def get_ip_information(ip):
    url1 = 'http://api.map.baidu.com/highacciploc/v1?qcip=' + ip + '&qterm=pc&ak=百度key&coord=bd09ll&extensions=3'
    poiss = ''
    request = urllib2.Request(url1)
    page = urllib2.urlopen(request, timeout=10)
    data_json = page.read()
    data_dic = json.loads(data_json)

    if (data_dic.has_key("content")):
        content = data_dic["content"]
        address_component = content["address_component"]
        location = content["location"]
        formatted_address = content["formatted_address"]
        print "该IP地址的具体位置为："
        print address_component["country"]
        lat = location["lat"]
        lng = location["lng"]
        print lat
        print lng
        print formatted_address
        url = 'http://api.map.baidu.com/staticimage/v2?ak=百度key&mcode=666666&center=' + str(
            lng) + ',' + str(lat) + '&markers=' + str(lng) + ',' + str(lat) + '&width=800&height=800&zoom=19'
        file = cStringIO.StringIO(urllib2.urlopen(url).read())
        img = Image.open(file)
        img.show()

        if (content.has_key("pois")):
            print "该IP地址附近POI信息如下："
            pois = content["pois"]
            for index in range(len(pois)):
                pois_name = pois[index]["name"]
                pois_address = pois[index]["address"]
                print pois_name, pois_address
    else:
        print 'IP地址定位失败！！！'


if __name__ == '__main__':
    ip = raw_input("Please input the IP:")
    get_ip_information(ip)