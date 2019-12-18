"""
示例
"""


import pymysql

db=pymysql.connect(host="localhost",port=3306,user="root",
                     password= "123456",database="dict",charset=
                     "utf8")

cur = db.cursor()
list1 = []
f = open("dict.txt")
num = 1
for line in f:
    d = line.split(" ",1)[0]
    w = line.split(" ",1)[1]
    list1.append((num,d,w))
    num +=1
f.close()
sql = "insert into words values(%s,%s,%s)"
try:
    cur.executemany(sql,list1)
    db.commit()
except:
    db.rollback()

cur.close()
db.close()

