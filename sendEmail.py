#!/usr/bin/python3.6

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

receipents=[]
with open('test.csv', 'rb') as csvfile:
	for i in csvfile.readlines():
		temp=i.decode('utf-8').split(',')
		receipents.append([temp[1].strip(), temp[3].strip()])

del receipents[0]

emailBody=input("Enter email body in html format: ")
print('\n')

senderEmailAddress=''
senderEmailPassword=''

emailSubjectLine='Test email'

for receipent in receipents:
	print("Sending email to: "+receipent[1])
	msg=MIMEMultipart()
	msg['From']=senderEmailAddress
	msg['To']=receipent[1]
	msg['Subject']=emailSubjectLine
	emailBody=emailBody.replace('kuberiter-mail-client', receipent[0])

	msg.attach(MIMEText(emailBody, 'html'))

	emailContent=msg.as_string()
	server=smtplib.SMTP('smtp-mail.outlook.com:587')

	server.starttls()
	server.login(senderEmailAddress, senderEmailPassword)

	server.sendmail(senderEmailAddress, receipent[1], emailContent)
	server.quit()
	print("Sent for email: "+receipent[1])
