import threading, time


class NewThread(threading.Thread):
    def __init__(self, threadName, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.sleepTime = sleepTime

    def run(self):
        num = 0
        while num < 5:
            localtime = time.localtime()
            info = time.strftime("%I:%M:%S", localtime)
            print(self.threadName, num, info)
            time.sleep(self.sleepTime)
            num += 1
            if num == 3: break
        print(self.threadName, " ended")


thread1 = NewThread("Wątek 1", 1)
thread2 = NewThread("Wątek 2", 1)
thread1.start()
thread2.start()

time.sleep(1)
print("-- Wątek 2 status: ", thread2.is_alive())  #sprawdza czy wątek działa

thread1.join()
thread2.join()
