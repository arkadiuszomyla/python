#klasa dziedziczy właściwości z klasy Exception
class BITException(Exception):
    def __init__(self, text, area):
        super().__init__(text)
        self.area = area

    def __str__(self):
        return "{}, area {}".format(super().__str__(), self.area)

class BITSecurityException(BITException):
    pass

class BITDataFormatException(BITException):
    pass

try:
    #do something
    raise BITException("file format is incorrent")
except BITException as e:
    print("Application error: {}".format(e))

try:
     # do something
     raise BITException("file format is incorrent", "Financial data")
except BITSecurityException as e:
    print("Application security error: {}".format(e))
except BITDataFormatException as e:
    print("Application data malformed error: {}".format(e))
except BITException as e:
     print("Application error: {}, area {}".format(e, e.area))
except Exception as e:
    print("General error: {}".format(e))


