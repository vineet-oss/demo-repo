# This is a main script.
# It will help to insert Email in DB

import insertemail;
import  dbconnect;


def main_script():
    # print('Python Script is started ')
    isemail = input('You want to send mails ? [Y/n]')
    if isemail == 'Y':
        insertemail.insert_email_db()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     main_script();
