import threading

def run():
    for x in range(100):
        print(x)
    
if __name__ == '__main__':
    myThread1 = threading.Thread(target=run)
    myThread1.start()
    myThread2 = threading.Thread(target=run)
    myThread2.start()