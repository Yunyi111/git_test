# define Python user-defined exceptions
class Error(Exception):
    pass
class ValueTooSmallError(Error): #ValueTooSmallError is a type of Error
    pass

num=-3

try:
    if num<0:
        raise ValueTooSmallError

except ValueTooSmallError:
    print("you reached this because the value was too small.")
except Exception as e:
    print("an unknown error has occurred "+str(e))