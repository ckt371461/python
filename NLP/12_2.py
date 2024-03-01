import jieba
text1='我去過清華大學及交通大學'
text2='小明來到了航研大廈'
seg_list=jieba.cut(text1,cut_all=True,HMM=False)
print("Full mode"+'/'.join(seg_list))
seg_list=jieba.cut(text1,cut_all=False,HMM=False)
print('/'.join(seg_list))
seg_list=jieba.cut(text1,cut_all=False,HMM=True)
print("Default mode"+'/'.join(seg_list))

print(','.join(jieba.cut(text2,HMM=True)))
print(','.join(jieba.cut(text2,HMM=False)))
print(','.join(jieba.cut(text2)))
print(','.join(jieba.cut_for_search(text2)))#透過網路資料分詞




