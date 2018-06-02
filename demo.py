import requests
import jieba
from bs4 import BeautifulSoup
url='http://tech.sina.com.cn/i/2018-06-02/doc-ihcikcew4437007.shtml'
res=requests.get(url)
res.encoding = "utf8"
soup = BeautifulSoup(res.text,"html.parser")
content = soup.find('div', id='artibody')
# print(soup.p.contents)
for p in soup.select('p'):
    text=p.get_text()
    print("原句："+text)
    seg_list = jieba.cut(text, cut_all=True)
    print("全模式：" +"/".join(seg_list))
    seg_list = jieba.cut(text)
    print("精准模式：" + "/".join(seg_list))
