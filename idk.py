#app.py
import mysql.connector as m
con=m.connect(host='localhost',user='root',passwd='mag26751!',database='hello')


cursor=con.cursor()
st='show tables'
#
cursor.execute(st)
y=cursor.fetchall()
print(y)
for i in y:
	print(i)