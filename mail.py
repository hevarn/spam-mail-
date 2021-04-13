#'islc nbug kbjg lavt'

#incorporé fichier html

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tqdm import tqdm


#fonction mail
def mail(n):
    #main text html
    email_body_header = ' '
    email_body_header = email_body_header + '<html><head></head><body>'
    email_body_header = email_body_header + '<style type="text/css">' '</style>'
    email_body_header = email_body_header + '<br><p>Hello Team,<br><br>This is a test email.<br>'
    email_body_content = ' '
    email_body_content = email_body_content + '<H1>This is main content area</h1>'
    email_body_footer = ' '
    email_body_footer = email_body_footer + '<br>Thank you'
    email_body_footer = email_body_footer + '<br>Support Team<br>'
    email_body = str(email_body_header) + str(email_body_content) + str(email_body_footer)
    #main part protocol smtp
    message = MIMEMultipart('alternative')
    body = email_body
    message.attach(MIMEText(body, 'html'))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('hevarn25@gmail.com','islc nbug kbjg lavt')
    mailserver.sendmail('hevarn25@gmail.com','hevarn25@gmail.com', message.as_string())
    mailserver.quit()

#loop whith module tqdm
for i in tqdm(range(100)):
    mail(1)


print("mail envoyé")



