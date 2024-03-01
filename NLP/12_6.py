import jieba,jieba.analyse
from os import path
d=path.dirname(__file__)
text='柯博文老師，喜歡去「甜心一點DIY烘培坊」做蛋糕。'
jieba.load_userdict(path.join(d,'userdict.txt'))
print('default'+'='*40)
results=jieba.tokenize(text) #取出斷詞位置
for result in results:
    print(f'word {result[0]} start {result[1]} end {result[2]}')
print('tokenize search'+'='*40)
results=jieba.tokenize(text,mode='search')
for result in results:
    print(f'word {result[0]} start {result[1]} end {result[2]}')
print('default idf'+'='*40)
keywords=jieba.analyse.extract_tags(text,topK=10,withWeight=True,allowPOS=())
print(f'TopK=TF/IDF , Tf ={len(keywords)}')
for item in keywords:
    print(f'{item[0]}, TF={item[1]}')
print('set idf'+'='*40)
jieba.analyse.set_idf_path('idf.txt')
keywords=jieba.analyse.extract_tags(text,topK=10,withWeight=True,allowPOS=())
for item in keywords:
    print(f'{item[0]}, TF={item[1]},IDf={len(keywords)*item[1]},topK={item[1]*len(keywords)*item[1]}')

