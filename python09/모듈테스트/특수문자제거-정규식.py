#일정 시간 간격으로 크롤링 및 기타 반복 작업 가능한 예제
import time
import threading

def thread_run():
    print('=====',time.ctime(),'=====')
    for i in range(1,1000):
        print('스레드 실행 중.. - ', i)
        threading.Timer(5, thread_run).start()

thread_run()