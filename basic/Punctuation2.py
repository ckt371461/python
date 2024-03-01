import string
def p(str_1):
    punc = string.punctuation
    if str_1 in punc:
        return True
    else:
        return False
def remove(str_2):
    l = []
    for s in str_2:
        if not p(s):
            l.append(s)
    return ''.join(l)

print(remove('ab,c'))

        