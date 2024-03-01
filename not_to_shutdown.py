
def main():
    from os import system 
    system('shutdown -a')
if __name__=='__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()