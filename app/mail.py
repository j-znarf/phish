import smtplib
from email.mime.text import MIMEText


def sendmail(smtp_params, sender, receivers):
    msg = MIMEText('This is test mail')

    msg['Subject'] = 'Test mail'
    msg['From'] = sender
    msg['To'] = receivers[0]

    with smtplib.SMTP(smtp_params[0], smtp_params[1]) as server:
        try:
            server.starttls()
        except smtplib.SMTPNotSupportedError:
            print('Server does not support STARTTLS')
        server.ehlo('example.com')
        server.sendmail(sender, receivers, msg.as_string())