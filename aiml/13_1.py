import aiml
kernel=aiml.Kernel()
kernel.learn('AIML-hello.xml')
while True:
    print(kernel.respond(input('Enter your message >>')))
#將 aiml 原檔裡面的 time.clock() 都改成 time.perf_counter() (Python 3.8 後不支援time.clock())
