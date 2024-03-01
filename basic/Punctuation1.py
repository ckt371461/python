import string
def p(str_1):
    punc = string.punctuation
    if str_1 in punc:
        return True
    else:
        return False
print(p("."))