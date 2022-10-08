import requests
from lxml import etree
import json,os
server = "http://www.xhhongmingsl.com"
url = 'http://www.xhhongmingsl.com/index.php/list-9'
res = requests.get(url)
e = etree.HTML(res.text)
li_list = e.xpath("//ul[@class='expmenu']/li")
print(li_list)
product = []

for li in li_list:
    di = {}
    title = li.xpath(".//div/a/text()")
    href = li.xpath('.//div/a/@href')
    second_li = li.xpath(".//ul/li")
    di["title"] = title[0]
    di["href"] = href[0]
    di['child'] = []
    path = 'product/' + title[0]
    try:
        os.mkdir(path)
    except:
        pass

    if second_li:
        for sc in second_li:
            sc_di = {}
            sc_title = sc.xpath(".//a/text()")
            sc_href = sc.xpath('.//a/@href')
            sc_di["sc_title"] = sc_title[0]
            sc_di["sc_href"] = sc_href[0]
            di['child'].append(sc_di)
            path2 = path + '/' + sc_title[0]
            try:
                os.mkdir(path2)
            except:
                pass
            c_url = server + sc_href[0]

            while c_url:
                c_res = requests.get(c_url)
                c_e = etree.HTML(c_res.text)
                c_li_list = c_e.xpath(".//div[@class='prolist']/ul/li")
                for pic in c_li_list:
                    file_href = pic.xpath(".//a/img/@src")[0]
                    # filename = pic.xpath(".//a/h3/text()")[0]
                    website = server + file_href
                    ff_name = file_href.split("/")[-1]
                    print(website)
                    ret = requests.get(url=website)
                    final = path2 + '/' + ff_name
                    with open(final,'wb') as f:
                        f.write(ret.content)
                if c_e.xpath("//a[contains(text(),'下一页')]/@href"):
                    c_url = server + c_e.xpath("//a[contains(text(),'下一页')]/@href")[0]
                else:
                    break


    else:
        # 爬虫当前分类
        c_url = server + href[0]

        while c_url:
            c_res = requests.get(c_url)
            c_e = etree.HTML(c_res.text)
            c_li_list = c_e.xpath(".//div[@class='prolist']/ul/li")
            for pic in c_li_list:
                file_href = pic.xpath(".//a/img/@src")[0]
                # filename = pic.xpath(".//a/h3/text()")[0]
                website = server + file_href
                ff_name = file_href.split("/")[-1]
                print(website)
                ret = requests.get(url=website)
                final = path + '/' + ff_name
                with open(final, 'wb') as f:
                    f.write(ret.content)
            if c_e.xpath("//a[contains(text(),'下一页')]/@href"):
                c_url = server + c_e.xpath("//a[contains(text(),'下一页')]/@href")[0]
            else:
                break


    product.append(di)
print(product)
