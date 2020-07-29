import smtplib, ssl
import imaplib
import getpass
import email
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


idlist=[]
try:
    #To connect to db
    conn = sqlite3.connect('ram1.db')
    c = conn.cursor() # Created cursor
    
    sender_address = "sacjau11@gmail.com"
    #To hide password while writing
    password = getpass.getpass(prompt='Enter your Password :: ')  
    mail = imaplib.IMAP4_SSL('imap.gmail.com')	
    mail.login(sender_address, password)
    mail.select() # connect to mailbox (default is 'INBOX').
    return_code, data = mail.search(None, 'UnSeen')
    
    mail_ids = data[0].decode()
    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    for i in range(latest_email_id,first_email_id -1, -1):
    
        typ, data = mail.fetch(str(i),'(RFC822)')
        for response_part in data:
           
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode("utf-8"))
                #print(msg)
                email_subject = msg['subject']
                email_from = msg['from']
                email_date = msg['date'] #date time
                idlist.append(email_from)
                #print([email_from, email_subject,email_date])

                #To Insert Email Information into db
                c.execute("INSERT INTO info(Mail_by,Subject, Day, Date, Time) VALUES (?,?,?,?,?)",(email_from,email_subject,email_date[:3],email_date[5:16],email_date[17:25]))

	      
except Exception as e: 
    print("As there is no unread Mail .",e)

#to commit all changes nd close the cursor
conn.commit()
conn.close()

#to extract unread email
send_id = []
for i in range(len(idlist)):
    mid = idlist[i].split("<")
    if len(mid) == 2:
        send_id.append(mid[1][:-1])
    else:
        send_id.append(mid[0])



# Create a secure TLS context and send mails
for i in range(len(send_id)):
	mail_Body = " Hy reply from bot, will contact you when we get free."
	message = MIMEMultipart()
	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.starttls()
	session.login(sender_address, password)
	#Email details
    message['From'] = sender_address
    message['To'] = send_id[i]
    message['cc'] = '2017cscloudsachin5788@poornima.edu.in'
    message['Subject'] = 'A test mail sent by Python.'
    message.attach(MIMEText(mail_Body, 'plain'))
    text = message.as_string()
    #print(text)
    session.sendmail(sender_address, send_id[i] , text)
    print('Mail Sent to : ',send_id[i])
	session.quit()

