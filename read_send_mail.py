import smtplib, ssl
import imaplib
import getpass
import email


idlist=[]
try:
    email_user = "sacjau11@gmail.com"
    #To hide password while writing
    password = input("password") #getpass.getpass(prompt='Enter your Password :: ')  
    mail = imaplib.IMAP4_SSL('imap.gmail.com')	
    mail.login(email_user, password)
    mail.select() # connect to mailbox (default is 'INBOX').
    return_code, data = mail.search(None, 'UnSeen')
    
    mail_ids = data[0].decode()
    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    for i in range(latest_email_id,first_email_id, -1):
    
        typ, data = mail.fetch(str(i),'(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode("utf-8"))
                email_subject = msg['subject']
                email_from = msg['from']
                idlist.append(email_from)
                print([email_from, email_subject])
	      
except Exception as e: print(e)

#to extract unread email
send_id = []
for i in range(len(idlist)):
    mid = idlist[i].split("<")
    if len(mid) == 2:
        send_id.append(mid[1][:-1])
    else:
        send_id.append(mid[0])



# Create a secure SSL context and send mails

for i in range(len(send_id)):
    messg= "Hy reply from bot, will contact you when we get free."
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", "465", context=context) as server:
        server.login(email_user, password)
        server.sendmail(email_user, send_id[i], messg)
