# This file help to send actual mail from python to users.

import smtplib


def send_email(to_email_list, alert_list):

    gmail_user = 'akash.smart247@gmail.com'
    gmail_password = 'sompra247@'

    sent_from = gmail_user
    to = to_email_list  # All list of Emails
    subject = 'Alert From Automated Detection System'
    body = alert_list

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')

    except:
        print('Something went wrong...')