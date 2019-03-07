
file=open('D:/lianxi/ciyun/xx.txt',encoding='utf-8', errors='ignore')
try:
    string=file.read()
finally:
    file.close()
print(type(string))
str=string.replace(" ",'')
str=str.replace("\n",'')
file=open('D:/lianxi/ciyun/xs.txt','a',encoding='utf-8')
for i in str:
    file.write(i)
file.close()
