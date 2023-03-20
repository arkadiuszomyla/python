class Door:

    def __init__(self, where):
        self.where = where

    def open(self):
        print('Opening door to the {}'.format(self.where))

    def close(self):
        print('Closing door to the {}'.format(self.where))


# door1 = Door('Hell')
# door2 = Door('Haven')
# door1.open()
# door1.close()
# door2.open()
# door2.close()

# with Door('hell') as door:
#    print(door.where)      #AttributeError: __enter__

from contextlib import contextmanager


@contextmanager
def OpenAndClose(obj):
    obj.open()
    yield obj
    obj.close()


with OpenAndClose(Door('hell')) as door:
    print(door.where)


################################################

@contextmanager
def OnlyClose(obj):
    yield obj
    obj.close()


with OnlyClose(Door('tuitam')) as door:
    door.open()
    print(door.where)

################################################

from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('http://www.kursyonline24.eu')) as page:
    for line in page:
        print(line)

################################################

import os
from contextlib import suppress

with suppress(FileNotFoundError):  # przekazuje wyjątek, który chce aby został ukryty
    os.remove(r'c:\temp\not_used_file.ext')

################################################

from contextlib import redirect_stdout

f = open(r'c:\temp\log.txt', 'w')
with redirect_stdout(f):            #umieszcza komunikat w pliku, bez wyświetlania na ekranie
    print('Hello')
    d = Door('EXIT')
    d.open()
    d.close()