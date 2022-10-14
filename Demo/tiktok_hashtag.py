import requests
from lxml import etree


url = "https://tiktokhashtags.com/index.php?"
data = {
    "h": "golang",
    "MM_update": "form1"
}
ret = requests.post(url, data=data)
with open("a.html", "wb") as f:
    f.write(ret.content)
e = etree.HTML(ret.content)
p1 = e.xpath("//section[@id='hashtag']//p1/text()")
p2 = e.xpath("//section[@id='hashtag']//p2/text()")
p1 = p1[0].strip() if p1 else ""
p2 = p2[0].strip() if p2 else ""
print(p1)
print(p2)

