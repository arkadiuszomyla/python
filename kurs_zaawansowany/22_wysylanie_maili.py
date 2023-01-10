# ominięta jedna lekcja o wysyłaniu maili z gmaila co już jest nieaktualne

import smtplib

mailFrom = 'Your automation system'
mailTo = ['1@gmail.com', '2@gmail.com']
mailSubject = 'Temat'
mailBody = '''Hello
This is mail
Have a nice day'''

message = '''From: {}
Subject: {}

{}'''.format(mailFrom, mailSubject, mailBody)

user = 'mailtestowy@gmail.com'
password = 'haslo'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')
