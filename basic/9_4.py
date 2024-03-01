class OopsException(Exception):
    pass


try:
    raise OopsException()
except:
    print("Caught an oops")
