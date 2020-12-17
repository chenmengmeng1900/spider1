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
    savepath = ".\\top250.xls"
    datalist = getData(baseurl)
    # oneurldata(baseurl)

    saveData(datalist,savepath)

# 影片链接
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)".*/>',re.S)

# 查找电影名字
findTitle = re.compile(r'<span class="title">(.*)</span>')

# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价
findJudge= re.compile(r'<span>(\d*?)人评价</span>')
#影片描述
findDis = re.compile(r'<span class="inq">(.*?)</span>')
# 找到影片相关内容
findDb = re.compile(r'<p class="">(.*?)<div class="star">',re.S)



def oneurldata(url):
    header ={
    # 'Accept-Encoding': 'gzip, deflate, sdch',
    # 'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Referer': 'http://www.wikipedia.org/',
    # 'Connection': 'keep-alive',
}

    request = urllib.request.Request(url,headers=header)

    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
    return html



# 爬取网页 获取数据
def getData(baseurl):
    datalist=[]
    for i in range(0,25):
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
                otitle = titles[1].replace("\n","")
                otitle = titles[1].replace("/","") # 添加外文名并去掉里面的符号

                data.append(otitle)
                # titles = re.sub("\n", " ", titles)
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

            Db = re.findall(findDb,item)[0]
            Db = re.sub('<br(\s+)?/>(\s+)?'," ",Db) #替换空格
            Db = re.sub("/"," ",Db)
            data.append(Db.strip()) #去掉空格

            datalist.append(data) #吧处理好的电影放入datalist



    return datalist





def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("sheet1",cell_overwrite_ok=True)  # 创建工作表
    col = ("影片连接","影片图片","影片名称","影片评分","影片评价","影片描述","影片内容")
    for i in range(0,7):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,7):
            sheet.write(i+1,j,data[j])
    book.save("top250.xls")


if __name__ == "__main__":
    main()
    print("抓取完毕")



