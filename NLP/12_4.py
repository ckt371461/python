import jieba,jieba.analyse,jieba.posseg,jieba.analyse.textrank
from os import path
d=path.dirname(__file__)#取得現在的路徑
text=open(path.join(d,'test.txt'),'r',encoding='utf-8').read()
text=text.replace(' ','')
text=text.replace('，','')
text=text.replace('。','')
print('/'.join(jieba.cut(text)))
print('1=============================')
jieba.load_userdict(path.join(d,'userdict.txt'))
print('/'.join(jieba.cut(text)))
print('2=============================')
words=jieba.posseg.cut(text)
for word,flag in words:
    print(f'{word},{flag}')
print('3=============================')
keywords1=jieba.analyse.extract_tags(text,topK=20,withWeight=True,allowPOS=())
for keyword in keywords1:
    print(keyword) 
    #print(f'{keyword[0]},{keyword[1]}')
print('4=============================')
keywords2=jieba.analyse.textrank(text,topK=20,withWeight=True,allowPOS=('n','s','vn','v'))#allowPOS表示輸出的範圍，不加不能輸出
for keyword in keywords2:
    print(f'{keyword[0]},{keyword[1]}')



