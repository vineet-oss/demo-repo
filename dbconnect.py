# This file is responsible to make connection with DB
# able to fetch records and insert records in DB.
# This file has 3 methods


import mysql.connector
from mysql.connector import Error

# DB Details
db_properties = mysql.connector.connect(host='localhost', database='snort', user='root', password='somesh')


def close_db(connection):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# this function return all Email ID from DB
def connect_db_getemail():
    try:
        lst = []  # Blank List
        connection = db_properties  # Get Connection object
        if connection.is_connected():
            cursor = connection.cursor()  # Get Cursor Object
            email_query = 'select * from  snort.emailtable where d_active=0'  # distinct(email)
            cursor.execute(email_query) # Execute OurQuery
            for i in cursor.fetchall():
                email = i[1]
                # print(email)
                lst.append(email)

        close_db(connection)  # Close Connection
        return lst

    except Error as e:
        print("Error while connecting to MySQL", e)


def connect_db_getotherdetails():
    try:
        lst = []  # Blank List
        connection = db_properties  # Get Connection object
        if connection.is_connected():
            cursor = connection.cursor()  # Get Cursor Object
            otherdetails_query = '''SELECT distinct 
                            s.sig_name,
                            concat('xxx.xxx.xxx.',SUBSTR(ip.ip_src, 8, 3)) AS ip_src,
                            concat('xxx.xxx.xxx.',SUBSTR(ip.ip_dst, 8, 3)) AS ip_dst
                            FROM 
                            signature s
                            JOIN event e ON s.sig_id = e.signature
                            JOIN iphdr ip ON e.cid = ip.cid
                            ORDER BY e.timestamp DESC '''  # distinct(email)
            cursor.execute(otherdetails_query)  # Execute OurQuery
            for i in cursor.fetchall():
                alertname = i[0]
                ip_src = i[1]
                ip_dst = i[2]
                print(alertname, ip_src, ip_dst)
                alert_string = ' --> ' + ip_src + ' --> ' + alertname + ' --> ' + ip_dst + '\n '
                lst.append(alert_string)
                lst.append(' :::: ')
                print(lst)

        close_db(connection)  # Close Connection
        return lst

    except Error as e:
        print("Error while connecting to MySQL", e)


def connect_db_insert(insert):
    # DB Details
    try:
        print('Connection Estatblish')
        connection = db_properties
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(insert)
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        print('Connection Close')
        close_db(connection)



"""
def email_count():
    try:
        connection = db_properties  # Get Connection object
        if connection.is_connected():
            cursor = connection.cursor()  # Get Cursor Object
            count_query = 'select distinct(email) from  snort.emailtable where d_active=0'
            i = cursor.execute(count_query)  # Execute OurQuery
            close_db(connection)  # Close Connection
            return i
        
    except Error as e:
        print("Error while connecting to MySQL", e)
        


#
#
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='snort',
#                                          user='root',
#                                          password='somesh')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         # record = cursor.fetchone()
#         # print("You're connected to database: ", record)
#
#
# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

"""