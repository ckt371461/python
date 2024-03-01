text='''title,author,year
TheWeirdstone of Brisingamen,AlanGarner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''
with open('books2.csv','w',encoding='utf-8') as infile:
    infile.write(text)

