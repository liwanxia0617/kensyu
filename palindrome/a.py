'''
ファイルの開き方

reader = open("in.txt","r",encoding="utf-8")
for line in reader:
    print(line,end="")
'''
with open(".\in.txt","r",encoding="utf-8") as reader:
    for line in reader:
        print(line,end="")

with open("out.csv","w",encoding="utf-8") as writer:
    print("test",file=writer)


#def main()
#    say_hello('syou')
#def say_hello(name)
'''
kakikata
'''
#print(f"konnnitiha{name}san")
#if__name == "__main__"
#say_hello("syou")

#pylintダウンロード
#python -m pip install --upgarade pylint
