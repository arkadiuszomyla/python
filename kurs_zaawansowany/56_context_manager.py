# with wywołuje automatycznie close
with open(r'C:\Users\arkadiuszo\PycharmProjects\python_nauka\kurs_zaawansowany\data.txt', 'w+') as file:
    file.writelines('SUCCESS')

try:
    with open(r'C:\Users\arkadiuszo\PycharmProjects\python_nauka\kurs_zaawansowany\da***ta.txt', 'w+') as file:
        file.writelines('SUCCESS')
except OSError as e:
    print('Error opening the file {}, details: {}'.format(e.filename, e.strerror))

########## BUDUJEMY WŁASNY CONTEXT MANAGER
import time


class time_measure:
    def __init__(self):
        pass

    # wywoluje się kiedy obiekt jest tworzony
    def __enter__(self):
        print('entering time: ')
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting..')
        self.__stop = time.time()
        self.__diffrence = self.__stop - self.__start
        print('Execution time: {}'.format(self.__diffrence))
        #return self.__stop, self.__diffrence


with time_measure() as my_timer:
    time.sleep(3)

