from collections import defaultdict
import re

path = "./in.txt"
words = defaultdict(int)
with open("out.csv", mode='w', encoding="utf-8") as writer:
    print("No,回文の文書,回文(かな),判定", file=writer)
    writer.close()
with open(path,'r+',encoding = 'utf-8') as reader:
    for i, element in enumerate(reader):
        j = i + 1
        atama = str(j) + ","
        for word in element.strip().split(' '):
            word = re.sub(r"\（",",",word)
            word1 = re.sub(r"\）",",",word)
            split_string = word.split(",")
            after_comma = split_string[1]
            pailindrome_word = re.sub(r"\）","",after_comma)
            d = reversed(list(pailindrome_word))
            if list(d) == list(pailindrome_word):
                word2 = (word1 +"〇")
                wordseikei = atama + word2
                with open("out.csv", mode='a', encoding="utf-8") as writer:
                    print(f"{wordseikei}",file=writer)
            else:
                word2= (word1 + "×")
                wordseikei = atama + word2
                with open("out.csv",mode='a',encoding="utf-8") as writer:
                    print(f"{wordseikei}",file=writer)
reader.close()
