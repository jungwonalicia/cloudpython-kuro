import pymysql

sum = 0
con = None 

'''1. db인증-> 연결'''
con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
print("1. db인증-> 연결  성공....")
print(con)

'''2. 연결정보-> 통로'''
cur= con.cursor()
print("2. 연결정보-> 통로 만들기 성공....")

'''3. sql문 만들어서 -> 전송'''
# sql1 = "insert into member values ('111', '111' ,'111', '111')"
# sql2 = "insert into member values ('222', '222' ,'222', '222')"
# sql3 = "insert into member values ('333', '333' ,'333', '333')"
sql = "insert into member values ('444', '444' ,'444')"
result = cur.execute(sql)
print("sql문 실행결과: ", result)
print("3. sql문 만들어서 -> 전송 성공....")

con.commit()

'''4. db 연결해제'''
con.close()
print("4. db 연결해제 성공....")
