hello = 'helloworld'
'''
スライス95P
'''

print(hello[0:4:])
print(hello[::1])
print(hello[::-1])

if hello[::-1] == hello:
    print("回文です")
