import aiml
kernel=aiml.Kernel()
kernel.learn('AIML-load.xml')
kernel.respond('load aiml b') #呼叫這個內容
while True:
    print(kernel.respond(input('Enter your message >>')))