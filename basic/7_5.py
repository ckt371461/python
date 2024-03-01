start1=["fee","fie","foe"]
rhymes=[
    ("flop","get a mop"),
    ("fope","turn the rope"),
    ("fa","get your ma"),
    ('fudge','call the judge'),
    ('fat','pet the cat'),
    ("fog","walk the dog"),
    ("fun","say we're done")
]
start2='Someone better'
start1_cap=[i.capitalize()+'!' for i in start1]
for rythem in rhymes:
    for i in range(len(start1_cap)):
        print(start1_cap[i],end='')
    print(rythem[0].capitalize()+'!') 
    print(start2,end=' ')   
    print(rythem[1]+'.')
