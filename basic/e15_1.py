import time
def wait_a_second(seconds):
    time.sleep(seconds)
    print(f'Wait {seconds} seconds , now is {time.time()}')
if __name__ == '__main__':
    for i in range(3):
        import multiprocessing as mp
        import random
        seconds=random.random()*5
        p=mp.Process(target=wait_a_second,args=(seconds,))
        p.start()

