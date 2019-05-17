import threading

def run(i):
    for x in range(100):
        print(i, ": ", x)
    
if __name__ == '__main__':
    myThread1 = threading.Thread(target=run, args=(1,))
    myThread1.start()
    myThread2 = threading.Thread(target=run, args=(2,))
    myThread2.start()