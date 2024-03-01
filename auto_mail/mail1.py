names_file = open("names.txt",'r',encoding = 'utf-8')
body_file = open("body.txt",'r',encoding = 'utf-8')

# read entire content of the body
body = body_file.read()

# iterate over names
for name in names_file:
    mail = "Hello "+name+body

    # write the mails to individual files
    mail_file = open('mail/'+name.strip()+".txt",'w',encoding = 'utf-8')
    mail_file.write(mail)