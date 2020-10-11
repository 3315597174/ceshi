#201841030138wang
import requests
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
RE=re.compile(r'<div class="contentbox" id="htmlContent">(.*?)<div class="ad00">',re.S)
RE2=re.compile(r'<h1>(.*?)</h1>',re.S)
def spider(index):
    url='https://www.duquanben.com/xiaoshuo/0/910/'+str(index)+'.html'
    res=requests.get(url)
    res=res.content.decode(encoding='gbk')
    res.encode('utf-8')
    soup=BeautifulSoup(res,'html5lib').prettify()
    result=str(soup)
    result=RE.findall(result)
    result=result[0]
    result=BeautifulSoup(result,'html5lib').prettify()
    result=result.replace('<html>','').replace('<head>','').replace('</head>','').replace('<br/>','').replace('<body>','').replace('</body>','').replace('</html>','')
    filename=RE2.findall(soup)
    filename=filename[0]
    filename=filename.replace(' ','').replace('\n','')
    filename2=filename
    filename='D:\\桌面\\1233\\'+filename+'.txt'
    file=open(filename,'w+',encoding='utf-8')
    file.write(result)
    print(filename2)
if __name__=='__main__':
    p=Pool(4)
    index = 4195702
    for i in range(index,index+2000):
        p.apply_async(spider, args=(i,))
    p.close()
    p.join()