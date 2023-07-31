from collections import defaultdict
import re
import sys

path = ".\in.txt"






#使える
#ファイル読み込む
#
#f = open(path,'r',encoding = 'utf-8')
#str = f.read()

words = defaultdict(int)

#word = re.sub(r"\(",",",str)

#print(word)

with open(path,'r',encoding = 'utf-8') as reader:
    for line in reader:
        for word in line.strip().split(' '):

#'カンマ後ろのデータ取得
            word = re.sub(r"\（",",",word)
            split_string = word.split(",")
            after_comma = split_string[1]
            migikakou = re.sub(r"\）","",after_comma)
            d = reversed(list(migikakou))
            if list(d) == list(migikakou):
                print(migikakou +"〇")
            else:
                print(migikakou+ "×")

            #if dx == migikakou:
                #print(migikakou +"〇")
            #else:
                #print(migikakou+ "×")



#回文判断方法１　テストOK
#s = input("字を入力してください")
#d = s[:: -1]
#if d == s:
#    print("〇")
#else:
 #   print("×")

            #word = re.sub(r"\）",",",word)

 #           words[word] += 1


#with open("out.csv","w",encoding="utf-8") as writer:
#    print("test",file=writer)


#path.close()
#words = defaultdict(int)

#with open(path,'r',encoding = 'utf-8') as reader:
 # for str in reader:
 #     a = re.sub(r"\(", ",", str)
 #     print(a)



#with open(path, encoding="UTF-8") as reader:
 #   for line in reader:
    #    for word in line.strip().split(' '):
    #line = re.sub(r"\(.*?\)", ",", line).lower()
 #       word = re.sub('\(.*?\)', '', word).lower()
  #      words[word] += 1
 #       print(word)
#line = re.sub('[?,!.]', '', line).lower().strip().split(' ')
    #print(line)
#print(line)
#line = print(line,end='１〇')
#print(str.split('('))
#print(str.split(')'))
#cut = re.sub('\('( ',', str))
#print(cut)


#print ("歌歌う（うたうたう）",end=",〇")



# 連続した小文字のアルファベットを置換
#ext = "abc123def456efg"
#result = re.sub(r'[a-z]+', "0", text)
#print(result)
#文書の行数計算

#count = 0
#for idx,line in enumerate(path):
#    count += 1
#print("ファイル行数は:",count)

# str = f.read()
#for line in str:
 #   line = print(str,end='〇')

    #line = re.sub('[?,!.]', '', line).lower().strip().split(' ')
    #print(line)
    #for word in line:
        #if word in words:
            #words[word] += 1

        #else:
            #words[word] = 0

#path.close()
