def test(func):
    def function(*args,**kargs):
        print('start')
        result=func(*args,**kargs)
        print('end')
        return result
    return function

@test
def get_odd():
    print("Greetings")

get_odd()
