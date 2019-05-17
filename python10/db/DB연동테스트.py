import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', password = '1234' ,db = 'cloud')
curs = conn.cursor()


sql = "insert into person values ('300', 'kim')" # 실행 할 쿼리문 입력
curs.execute(sql) # 쿼리문 실행

sql = "SELECT * FROM person" # 실행 할 쿼리문 입력
curs.execute(sql) # 쿼리문 실행

rows = curs.fetchall() # 데이터 패치

for i in rows :
    print(i)

conn.close()

