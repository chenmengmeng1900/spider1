from bs4 import BeautifulSoup
import re
file = open("./top250.html","r",encoding="utf-8")
html = file.read()
bs = BeautifulSoup(html,"html.parser")

print(bs.title)
print(bs.link)
print(bs.title.string)
print(bs.link.attrs) # 字段形式保存

# -----------------------------------------

# 应用
print("nihao")
print(bs.head.contents) # head 里面包含的一些东西s

print(bs.head.contents[1])

# descendants 孙子节点  strings  孙子节点的内容,strppered_strings  去掉多余空字符串
# parent 父节点, prents 递归得到所欲父节点,返回一个生成器

# previous_sibling 属性是字符串或者空白,真是结果是这个标签和上个标签之间的顿号和换行符
# next_sibling 当前节点的下一个节点
# previous_sibling 当前节点的所有的兄弟节点
# next_sibling 当前节点的下面的所有的兄弟节点
# has_attr 判断包含属性

# 文档搜索

# find_all
# find_all可以跟 属性,内容和参数
# 可以查找text里面的内容  a = bs.find_all(text="下载豆瓣客户端")或者 a = bs.find_all(text=["全新发布","Android","iPhone","读书"])
# finnd_all 配合正则表达式  a = bs.find_all(re.compile("\d"))

# .表示类属性,#表示id属性

#select css选择器搜索 bs.select(.class),bs.select(#id(里面的内容)) bs.select(a[class = "bri"])  bs.select("head > meta")   bs.select(".meta ～ meta")
#

t_list = bs.find_all("a")

t_list1 = bs.find_all(re.compile("a"))


def name_is_exist(tag):
    return tag.has_attr("name")
t_list2=bs.find_all(name_is_exist,limit = 10)


print(t_list2)

a = bs.find_all(text=["全新发布","Android","iPhone","读书"])
for  item in a:
    print(item)

b = bs.find_all(re.compile("\d"))

for item in b:
    print(item)

m = bs.select("head > meta")

for l in m:
    print(l)
print("测试自定义名字")

n=bs.select(".appintro-title~.qrcode")#不要用中间波浪线,要用上波浪线

print(n)


# .任意字符  *任意次数  c*  对前一个字符做限制   a{1} daf   a{1,2}  af aaf
# () 分组标记,只能有一个(a|b) a或者b  \w  {A-Za_z0-9_}

# re库里面常用的函数 search,find_all,match,split,sub替换,finditer()
# re.l 表示不区别大小写 re.S表示匹配换行符在内的所有字符
# re = re.compile("校验的标准")
# search = re.search("比对的内容")
# search = re.findall("al", "asjdfjalksdjk") #a表示要查找的内容,可以匹配全部.


print(re.sub("a", "A", "asdfaeqerqeKJahkjhkaAlkllkj999"))
# 字符串最好用 a = r"\sdafdadsfa交换空间'\;/"




