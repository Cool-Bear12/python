import json
# f=open("file.json","w", encoding="utf-8")
# #f.write("True")
#  conted =[None,True,(1,2,3),[1,2,3],"hello","привки"]
#  json.dump(conted,f, ensure_ascii=False)# в json и в файл
# print(json.dump(conted))
# f.close()
#
# readF= open("file.json","r",encoding="utf=8")
# #print(readF.read())
# print(json.load(readF))
# readF.close()

#задача1
readF= open("file.txt","r",encoding="utf=8")
contetnt=readF.readlines()
readF.close()
print(contetnt)
d={}
for record in contetnt:
    splited=(record.split(": "))
    d[splited[0]]=splited[1].rstrip()
print(d)
f = open("file.json","w", encoding="utf-8")
json.dump(d, f, ensure_ascii=False)
f.close()