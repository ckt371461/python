import jieba,jieba.analyse
from os import path
d=path.dirname(__file__)
text=open(path.join(d,'test.txt'),'r',encoding='utf-8').read()
text=text.replace('\n','')
jieba.analyse.set_stop_words('stop_words.txt')
print('/'.join(jieba.cut(text)))
print('='*20)
jieba.load_userdict(path.join(d,'userdict.txt'))
dic=dict()
for element in jieba.cut(text):
    if element not in dic:
        dic[element]=1
    else:
        dic[element]+=1
'''sorted(iterable, cmp=None, key=None, reverse=False)
参数说明：
iterable -- 可迭代对象。
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）'''
for element in sorted(dic,key=dic.get,reverse=True):
    print(element,dic[element])


