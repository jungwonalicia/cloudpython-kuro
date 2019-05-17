import datetime

# 1. 지금 몇 시인인지 처리
now = datetime.datetime.now()
hour = now.hour
print(hour)

# 2. 지금 시각이 22시 전인가요?. 
#      true: 아직 집에 갈 시간이 멀었군요.
#      false: 집에 갈 시각이군요.

if hour <= 22:
    print("아직 집에 갈 시간이 멀었군요.")
else:
    print("집에 갈 시각이군요.")
# 
# 시각 처리 프로그램 종료







