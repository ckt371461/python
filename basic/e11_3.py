from collections import defaultdict
dict_of_lists=defaultdict(list)
#要使用append，因為性質設定為list
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])