# This is mail python file which is responsible to send mail
# Call this file from CRON Express to send mail.

import dbconnect
import sendmail


def send_mail():
    # Get List of Emails
    email_list = dbconnect.connect_db_getemail();
    print(email_list)
    # Get list of Alerts
    alert_list = dbconnect.connect_db_getotherdetails()
    print(alert_list)
    # Send Mail
    sendmail.send_email(email_list, alert_list)


if __name__ == '__main__':
    send_mail()
