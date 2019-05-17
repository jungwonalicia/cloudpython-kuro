'''
1. 태어난 해를 입력
2. 나이를 계산(year이용)
3. 나이가 18살 이상이면 성년
   미만이면 미성년
4. 성년/미성년 판별 프로그램 종료합니다. 프린트
'''
import datetime
now = datetime.datetime.now()

# 1
birth = int(input("태어난 해를 입력>>> "))

# 2
age = now.year - birth + 1
print("나의 나이는 ", age)

# 3. 나이가 18살 이상이면 성년, 미만이면 미성년
if age >= 18:
    gender = input("당신의 성별은 ")
    if gender == "남":
        print("남자 성년")
    else:
        print("여자 성년")
else:
    print("미성년")

# 4. 성년/미성년 판별 프로그램 종료합니다.
print("성년/미성년 판별 프로그램 종료합니다.")





