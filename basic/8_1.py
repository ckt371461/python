e2f={
    'dog':'chien',
    'cat':'chat',
    'walrus':'morse'
}
print(e2f['walrus'])
f2e=dict()
for english,french in e2f.items():
    f2e[french]=english
print(f2e['chien'])    
english_keys=set(e2f.keys())
print(english_keys)