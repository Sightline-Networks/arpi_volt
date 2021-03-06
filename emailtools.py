import subprocess
import smtplib
import json
from email.mime.text import MIMEText


class EmailTools():
    def __init__(self, config):
        self.config = config


    def send_email(self, to, subject, body):
        msg = MIMEText(body)
        msg['Subject']    = subject
        msg['From']       = self.config['email']['from']
        msg['To']         = to
        msg['Body']       = body
        msg['Precedence'] = 'bulk'
        msg['Auto-Submitted'] = 'auto-generated'
        s = smtplib.SMTP('localhost')
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()




if __name__ == '__main__':
    with open('config', 'r') as cfg:
        config = json.loads(cfg.read())

        e = EmailTools(config)
        e.send_email(config['email']['to'], 'RP up', 'some message')

