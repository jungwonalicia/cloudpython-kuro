import pymysql

def db_select(id):
    con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
    print("1. db인증-> 연결  성공....")
    print(con)
    
    '''2. 연결정보-> 통로'''
    cur= con.cursor()
    print("2. 연결정보-> 통로 만들기 성공....")
    
    '''3. sql문 만들어서 -> 전송'''
    sql = "select * from member where id = '"+ id + "'"
    print("생성된 sql:", sql)
    cur.execute(sql) 
    print("3. sql문 만들어서 -> 전송 성공....")
    
#     con.commit()
    
    record = cur.fetchone()
    print(record)
    
    print(record[0], record[1], record[2], record[3])
    '''4. db 연결해제'''
    con.close()
    print("4. db 연결해제 성공....")
    return record

def db_select_all():
    con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
    print("1. db인증-> 연결  성공....")
    print(con)
    
    '''2. 연결정보-> 통로'''
    cur= con.cursor()
    print("2. 연결정보-> 통로 만들기 성공....")
    
    '''3. sql문 만들어서 -> 전송'''
    sql = "select * from member"
    print("생성된 sql:", sql)
    n = cur.execute(sql) 
    print("3. sql문 만들어서 -> 전송 성공....")
    result = []
#     con.commit()
    while True:
        record = cur.fetchone()
        if record == None:
            break
        else:
            print(record)
            result.append(record)
        
           
#     print(result)
    
    '''4. db 연결해제'''
    con.close()
    print("4. db 연결해제 성공....")
    return result
    
def db_insert(id, pw, name, tel):
    '''1. db인증-> 연결'''
    con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
    print("1. db인증-> 연결  성공....")
    print(con)
    
    '''2. 연결정보-> 통로'''
    cur= con.cursor()
    print("2. 연결정보-> 통로 만들기 성공....")
    
    '''3. sql문 만들어서 -> 전송'''
    sql = "insert into member values ('"+ id + "', '" + pw + "', '" + name + "', '" + tel +"')"
    print("생성된 sql:", sql)
    cur.execute(sql) 
    print("3. sql문 만들어서 -> 전송 성공....")
    
    con.commit()
    
    '''4. db 연결해제'''
    con.close()
    print("4. db 연결해제 성공....")
    
def db_delete(id):
    '''1. db인증-> 연결'''
    con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
    print("1. db인증-> 연결  성공....")
    print(con)
    
    '''2. 연결정보-> 통로'''
    cur= con.cursor()
    print("2. 연결정보-> 통로 만들기 성공....")
    
    '''3. sql문 만들어서 -> 전송'''
    sql = "delete from member where id = " + id
    print("생성된 sql:", sql)
    cur.execute(sql) 
    print("3. sql문 만들어서 -> 전송 성공....")
    
    con.commit()
    
    '''4. db 연결해제'''
    con.close()
    print("4. db 연결해제 성공....")
    
def db_update(id, pw, name, tel):
    '''1. db인증-> 연결'''
    con = pymysql.connect(host ='localhost', user = 'root', password = '1234', db = 'cloud')
    print("1. db인증-> 연결  성공....")
    print(con)
    
    '''2. 연결정보-> 통로'''
    cur= con.cursor()
    print("2. 연결정보-> 통로 만들기 성공....")
    
    '''3. sql문 만들어서 -> 전송'''
    sql = "update member set pw = " + pw + ", name = " + name + ", tel = "  + tel + " where id = " + id
    print("생성된 sql:", sql)
    cur.execute(sql) 
    print("3. sql문 만들어서 -> 전송 성공....")
    
    con.commit()
    
    '''4. db 연결해제'''
    con.close()
    print("4. db 연결해제 성공....")

if __name__ == '__main__':
    print("회원가입 정보를 입력해주세요.")
    print("----------------------")
    id = input("ID입력>> ")
    pw = input("PW입력>> ")
    name = input("NAME입력>> ")
    tel = input("TEL입력>> ")
    db_insert(id, pw, name, tel)
    
    print("-----------------------")
    id = input("삭제할 ID입력>> ")
    db_delete(id)
    
    print("-----------------------")
    id = input("수정할 ID입력>> ")
    pw = input("수정할  PW입력>> ")
    name = input("수정할  NAME입력>> ")
    tel = input("수정할  TEL입력>> ")
    db_update(id, pw, name, tel)
    
    
    
    
    
    



