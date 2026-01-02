# -*- coding: utf-8 -*-
import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from config.config import get_config
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

class EmailClient:
    def __init__(self, provider='gmail'):
        self.cfg = get_config(provider)
        self.email = self.cfg['SENDER_EMAIL']
        self.password = self.cfg['SENDER_PASSWORD']
        self._connect()
    
    def _connect(self):
        self.smtp = smtplib.SMTP(self.cfg['smtp_server'], self.cfg['smtp_port'])
        context = ssl.create_default_context()
        self.smtp.starttls(context=context)
        self.smtp.login(self.email, self.password)
        print(f' Connected: {self.cfg["smtp_server"]}:{self.cfg["smtp_port"]}')
    
    def send_email(self, to, subject, body, is_html=False):
        recipients = [to] if isinstance(to, str) else to
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html' if is_html else 'plain'))
        self.smtp.sendmail(self.email, recipients, msg.as_string())
        print(f' Email SENT to {len(recipients)} recipient(s)!')
        self.smtp.quit()
        return {'status': 'success', 'recipients': recipients}

if __name__ == '__main__':
    client = EmailClient('gmail')
    client.send_email('test@example.com', 'Fixed! ', 'UTF-8 clean!')
