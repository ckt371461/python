from opencc import OpenCC
text1='印表機 光碟 記憶體'
text2='打印机 光盘 内存'
openCC=OpenCC('t2s') #traditional to simple  繁轉簡體
line1=openCC.convert(text1)
print(f'text1 = {text1}')
print(f'text1 through t2s ={line1}')
line1=openCC.set_conversion('tw2sp')#可以這樣切換
line1=openCC.convert(text1)
print(f'text1 through tw2sp ={line1}')

opencc=OpenCC('s2twp')
print(f'text2 = {text2}')
line2=opencc.convert(text2)
print(f'text2 through s2twp ={line2}')
