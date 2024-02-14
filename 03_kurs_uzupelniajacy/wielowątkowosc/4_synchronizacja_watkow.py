import threading, time

data = ["ola", "Ala", "Kasia", "Tola", "Marek"]
dataLock = threading.Lock()  # pozwoli na zastosowanie acquire i release

class NewThread(threading.Thread):
    def __init__(self, threadName, dataLen, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleepTime = sleepTime

    def run(self):
        num = 0
        while num < self.dataLen:
            dataLock.acquire()   #zmusza wszystkie wątki aby zaczęły działać synchronicznie dla danego kawałka kodu, zaczyna blokowanie dla konkretnego wątku
            print(self.threadName, data[num])    #wątki wspólnie odwołują się tylko do tej linijki
            dataLock.release()    #zwalnia blokowanie zasobu
            time.sleep(self.sleepTime)
            num += 1
        print(self.threadName, " ended")


thread1 = NewThread("Wątek 1", len(data), 1)
thread2 = NewThread("Wątek 2", len(data), 1)
thread1.start()
thread2.start()

time.sleep(1)
print("-- Wątek 2 status: \n", thread2.is_alive())  #sprawdza czy wątek działa

thread1.join()
thread2.join()