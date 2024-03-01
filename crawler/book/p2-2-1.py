filename = 'info.csv'
data = list()
with open(filename,'rt') as fp:
    '''
    read():
    1、读取整个文件，返回的是一个字符串，字符串包括文件中的所有内容。
    2、若想要将每一行数据分离，即需要对每一行数据进行操作，此方法无效。
    3、若内存不足无法使用此方法。
    readline():
    1、每次读取下一行文件。
    2、可将每一行数据分离。
    3、主要使用场景是当内存不足时，使用readline()可以每次读取一行数据，只需要很少的内存。   
    readlines():
    1、一次性读取所有行文件。
    2、可将每一行数据分离，从代码中可以看出，若需要对每一行数据进行处理，可以对readlines()求得的结果进行遍历。
    3、若内存不足无法使用此方法。
    '''
    columns = fp.readline().split(",")#讀第一行
    '''print str.split( );       # 以空格为分隔符，包含 \n
    print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
    以上实例输出结果如下：

    [ 'Line1-abcdef', 'Line2-abc', 'Line4-abcd']
    ['Line1-abcdef', '\nLine2-abc \nLine4-abcd']'''
    for item in fp.readlines():
        temp = dict()
        for number,datum in enumerate(item.split(",")):
            temp[columns[number].strip()]=datum.strip() 
            #Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
            #注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
            # 這裡用來刪除字尾的換行符號
            data.append(temp)
    print(data)