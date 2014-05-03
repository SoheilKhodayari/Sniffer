import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

class emailSender():
    def __init__(self, user=None, pwd=None, smtpServer=None, port=None):
        self.user = user
        self.pwd = pwd
        self.smtpServer = smtpServer
        self.port = port

    def setUser(self, user):
        self.user = user

    def setPwd(pwd):
        self.pwd = pwd

    def setSmtp(self, smtpServer):
        self.smtpServer = smtpServer

    def setPort(port):
        self.port = port

    def send(self, to, subj=None, body=None, attach=None):
        if subj is None:
            subj = "no subject"
        if body is None:
            body = "no body"

        msg = MIMEMultipart()

        msg['From'] = self.user
        msg['To'] = to
        msg['Subject'] = subj
        msg.attach(MIMEText(body))

        if attach != None:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                'attachment; filename="%s"' % os.path.basename(attach))
            msg.attach(part)

        mailServer = smtplib.SMTP(self.smtpServer, self.port)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.login(self.user, self.pwd)
        mailServer.sendmail(self.user, to, msg.as_string())
        mailServer.close()

#email=emailSender('asoheil59@yahoo.com','9759865','smtp.yahoo.com','PORT') #enter port here

#email.send()
