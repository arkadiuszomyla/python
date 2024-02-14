import threading, time

def printTime(threadName, sleepTime):
    num = 0
    max = 6
    while num < max:
        localTime = time.localtime()
        print(threadName, time.strftime("%H %M %S", localTime))
        time.sleep(sleepTime)

        num += 1
    print(threadName, " ended")

t1 = threading.Thread(target= printTime, args= ("Wątek 1", 0.5))
t2 = threading.Thread(target= printTime, args= ("WĄTEK 666", 0.2))

t1.start() #rozpoczyna wątek
t2.start()

print("Głowny wątek programu poczeka na zakończenie t1, t2\n")
t1.join()
print("T1 endend")
t2.join()
print("T2 endend")

print("Main prog ended")

