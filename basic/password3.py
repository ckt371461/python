a = 0
while a < 3:
    name = input("請輸入使用者名稱： ")
    password = input("請輸入密碼: ")
    a  = a + 1
    if name == 'wxd' and password == '123456':
        print("登陸成功")
        exit()
    else:
        print("輸入錯誤，請重新輸入")
print("輸入錯誤三次，退出")