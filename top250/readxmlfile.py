import sys
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt


# file = open("./top250.html","r",encoding="utf-8")
# html = file.read()


def main():
    # 其实就是主类，吧所有的赋值后的参数放进来
    baseurl = "https://movie.douban.com/top250?start="
    # 用双斜杠或者前面加r
    savepath = "./top250.html"
    # oneurldata(baseurl)
    getData(baseurl)

# 影片链接
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?">)',re.S)
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片名字

#影片评价
findJudge= re.compile(r'<span>(\d*?)人评价</span>')
#影片描述
findDis = re.compile(r'<span class="inq">(.*?)</span>')
# 找到影片相关内容
findDb = re.compile(r'<p class="">(.*?)<div class="star">',re.S)
# 查找电影名字
findTitle = re.compile(r'<span class="title">(.*)</span>')


def oneurldata(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

    request = urllib.request.Request(url,headers=header)

    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
    return html



# 爬取网页 获取数据
def getData(baseurl):
    datalist=[]
    for i in range(0, 1):
        url = baseurl + str(i*25)
        html = oneurldata(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            data=[] #存一步电影的数据
            item = str(item)

            # print(item)
            # break
            link = re.findall(findLink, item)[0]
            data.append(link)
            # print(link)
            ImgSrc = re.findall(findImgSrc,item)[0]
            data.append(ImgSrc)
            titles = re.findall(findTitle,item)
            if len(titles)==2:
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/","")  # 添加外文名并去掉里面的符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ') # 留空.
            Rating = re.findall(findRating,item)[0]
            data.append(Rating)
            Judge = re.findall(findJudge,item)
            data.append(Judge)
            Dis = re.findall(findDis,item)
            if len(Dis) != 0:
                Dis = Dis[0].replace(".", "")
                data.append(Dis)
            else:
                data.append(" ")

            Db = re.findall(findDb,item)
            Db = re.sub('<br(\s+)?/',)
            data.append(Db)
            Title = re.findall(findTitle,item)
            Title = re.trim(Title)
            Title = re.sub("\n", "")
            data.append(Title)



    return datalist





def saveData(savepath):
    pass


if __name__ == "__main__":
    main()



