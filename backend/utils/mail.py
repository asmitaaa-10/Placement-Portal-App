import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(to, subject, body, file_path=None, mime_type=None):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = "asmita.pal1010@gmail.com"
    msg['To'] = to
    msg.attach(MIMEText(body, 'html'))


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("asmita.pal1010@gmail.com", "njzl fyli tzti idkt")
        smtp.send_message(msg)

    return True