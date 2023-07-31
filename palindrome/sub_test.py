import re

s = "我是一个人(中国人)aaa[真的]bbbb{确定}"
s1 = "歌歌う（うたうたう）"
#s = "我是一个人(中国人)aaa[真的]bbbb{确定}"
#我是一个人〇aaa[真的]bbbb{确定}
#a = re.sub(r"\(.*?\)","〇",s)

#左(置き換え)
#s = "我是一个人(中国人)aaa[真的]bbbb{确定}"
#我是一个人〇中国人)aaa[真的]bbbb{确定}
a = re.sub(r"\(",",",s)

print(a)

s = a
#print(s)
b = re.sub(r"\)",",",s)
#print(b)
s = b
print(s)
#print(b)
#s = "我是一个人(中国人)aaa[真的]bbbb{确定}"
#我是一个人〇中国人)aaa[真的]bbbb{确定}
