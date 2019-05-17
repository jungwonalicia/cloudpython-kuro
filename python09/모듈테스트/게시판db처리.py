def create(id, title, content, writer):
    print("1. DB연결, 인증(id/pw)")
    sql = "insert into bbs values (" + id + ", " + title + ", " +content +  ", " + writer + ")"
    print("2.", sql, "문 실행 요청")
    print("3. DB연결 해제..")
    
def read(id):
    print("1. DB연결, 인증(id/pw)")
    sql = "select * from bbs where id = " + id 
    print("2. select문 실행 요청")
    print("3. 검색결과를 받아와서, 처리")
    print("4. DB연결 해제..")
#     return "select한 결과 반환.."

    result = []
    result.append(100) 
    result.append(100)
    result.append(100)
    result.append(100)
    return result

#     id = 100
#     title = 100
#     content = 100
#     writer = 100
#     return id, title, content, writer
    
def update():
    print("1. DB연결, 인증(id/pw)")
    print("2. update문 실행 요청")
    print("3. DB연결 해제..")
    
def delete():
    print("1. DB연결, 인증(id/pw)")
    print("2. delete문 실행 요청")
    print("3. DB연결 해제..")
        