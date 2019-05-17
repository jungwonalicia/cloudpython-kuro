import pymysql

'''1. db인증-> 연결'''
con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
print("1. db인증-> 연결  성공....")
print(con)

'''2. 연결정보-> 통로'''
cur= con.cursor()
print("2. 연결정보-> 통로 만들기 성공....")

'''3. sql문 만들어서 -> 전송'''
sql = "insert into member values ('500', '500' ,'500', '500')"
cur.execute(sql)
print("3. sql문 만들어서 -> 전송 성공....")

con.commit()

'''4. db 연결해제'''
con.close()
print("4. db 연결해제 성공....")
