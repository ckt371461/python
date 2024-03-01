def 回文(st):
    if st == st[::-1]:
        return True
    else:
        return False
print(回文("strrts"))
print(回文("strpps"))


