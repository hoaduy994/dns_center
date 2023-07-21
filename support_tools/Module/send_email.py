from main.models import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(Subject,name_file,email,uuidOne):
    mail_content = '''
        Test
    '''
    #The mail addresses and password
    sender_address = 'fis.security@fpt.com.vn'
    sender_pass = 'ACksURgAlkyl'
    receiver_address = email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = Subject
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))
    attach_file_name = '{}.zip'.format(name_file)
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'zip')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Disposition', 'attachment',filename='{}@{}.zip'.format(name_file,uuidOne))
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('mail.fpt.com.vn', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
