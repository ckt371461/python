from os import path
import jieba,jieba.analyse
d=path.dirname(__file__)
text='post部落格中將出錯，台中的名產中太陽餅是台中特產最出名'
text=text.replace('，','')
print('/'.join(jieba.cut(text)))
jieba.suggest_freq('台中',True) #設定"台中"這個詞
print('/'.join(jieba.cut(text)))
jieba.suggest_freq('名產',True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq('部落格',True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq('太陽餅',True)
print('/'.join(jieba.cut(text)))
jieba.suggest_freq(('中','將'),True)
print('/'.join(jieba.cut(text)))