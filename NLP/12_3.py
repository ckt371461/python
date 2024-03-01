import jieba,jieba.analyse,jieba.posseg 
#都要引用不然會出錯 AttributeError: module 'jieba' has no attribute 'analyse',#AttributeError: module 'jieba' has no attribute 'posseg'  
text='新北市板橋區的甜心一點DIY烘培坊是一家老師教你做甜點的蛋糕店'
print('/'.join(jieba.cut(text)))
#結果: 新/北市/板橋區/的/甜心/一點/DIY/烘培/坊/是/一/家/老師/教/你/做/甜點/的/蛋糕店
jieba.load_userdict('userdict.txt') #將新北市的idf分數提升至300,甜心一點DIY烘培坊提升至20
print('/'.join(jieba.cut(text)))
posseg=jieba.posseg.cut(text)
for item in posseg:
    print(item)
keywords=jieba.analyse.extract_tags(text,topK=20,withWeight=True,allowPOS=())#withWeight決定是否傳回泉種植，allowPOS決定是否過濾特定詞性
for item in keywords: 
    print(f'{item[0]} = {item[1]}')
