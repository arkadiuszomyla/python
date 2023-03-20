import smtplib
import functools

def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = '''From: {}
    Subject: {}

    {}'''.format(mailFrom, mailSubject, mailBody)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending email')
        return False


mailFrom = 'Your automation system'
mailTo = ['1@gmail.com', '2@gmail.com']
mailSubject = 'Temat'
mailBody = '''Hello
This is mail
Have a nice day'''
user = 'mailtestowy@gmail.com'
password = 'haslo'

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password) #nie trzeba będzie przekazywać wszystkich parametrów

SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody)

SendInfoEmailFromGmailWithSubject = functools.partial(SendInfoEmail, user, password, mailSubject) #nie trzeba będzie przekazywać wszystkich parametrów

SendInfoEmailFromGmailWithSubject(mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)