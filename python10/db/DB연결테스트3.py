import pymysql

try:
    '''1. db인증-> 연결'''
    con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
    print("1. db인증-> 연결  성공....")
    print(con)
    
    '''2. 연결정보-> 통로'''
    cur= con.cursor()
    print("2. 연결정보-> 통로 만들기 성공....")
    
    '''3. sql문 만들어서 -> 전송'''
    # sql2 = "select * from member "
    sql2 = "select * from test where id = '111'" #없는 테이블
    sql = "select * from member where id = '111'"
    
    result = cur.execute(sql2)
    print("sql문 실행결과: ", result)
    print("3. sql문 만들어서 -> 전송 성공....")
    
    # print(cur.fetchone())
    record = cur.fetchone()
    print("검색된 ID: ", record[0])
    print("검색된 PW: ", record[1])
    print("검색된 NAME: ", record[2])
    print("검색된 TEL: ", record[3])
    
    con.commit()
    
    '''4. db 연결해제'''
    con.close()
    print("4. db 연결해제 성공....")
except:
    print("에러발생===")
else:
    print("에러가 발생하지 않았음....")
