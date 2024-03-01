
def main():
    from os import system 
    system('shutdown -s -t 100')
if __name__=='__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()