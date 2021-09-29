# Email Insert Logic
import dbconnect


def insert_email_db():
    # number of emails as input
    n = int(input("Enter number of emails : "))

    # iterating till the range
    for i in range(0, n):
        print(i+1, ' of ', n)
        ele = input()
        insert_query = f'insert into snort.emailtable (email) values ( \'{ele}\')'  # Insert Query
        # print(insert_query)  # Query Print
        dbconnect.connect_db_insert(insert_query)  # Run Query
    print('All Emails are inserted')
