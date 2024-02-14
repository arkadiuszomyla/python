import _thread, time

def printTime(threadName, sleepTime):
    num = 0
    max = 6
    while num < max:
        localTime = time.localtime()
        print(threadName, time.strftime("%H %M %S", localTime))
        time.sleep(sleepTime)

        num += 1
    print(threadName, " ended")


_thread.start_new_thread(printTime, ("Wątek 1", 0.5))
_thread.start_new_thread(printTime, ("WĄTEK 666", 0.2))

while True:
   # if not _thread._count():
        pass


''' poza tematem, użycie schedulera:
import schedule
import time
from functools import wraps

def run_at_specific_time(hour, minute):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            schedule.every().day.at(f"{hour}:{minute}").do(func)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@run_at_specific_time(10, 30)
def my_function():
    print("Wywołano funkcję!")

while True:
    schedule.run_pending()
    time.sleep(1)
'''