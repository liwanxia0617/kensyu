

#せみをみせ
#def is_palindrone(s):
#    if len(s) <= 1:
 #       return True
 #   if s[0] != s[-1]:
 #       return False
 #   return is_palindrone(s[1:-1])


#回文判断方法１　テストOK
#s = input("字を入力してください")
#d = s[:: -1]
#if d == s:
#    print("〇")
#else:
 #   print("×")


#文書最後何付き
#s  = print(s ,end='〇')
s = input("文字をご入力してください:")
d = reversed(list(s))
if list(d) == list(s):
    print("〇")
else:
    print("×")
