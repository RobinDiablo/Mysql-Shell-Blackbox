import pymysql
import pandas
import shutil
import csv

hostname = 'localhost'
username = 'root'
password = 'rootpassword'
database = 'mysql'

conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
cur = conn.cursor()


def empty(file):
    f=open(f'C:/Users/balaji Vyshnavy/Desktop/evidence/{file}',mode='w+')
    f.truncate()
    f.close()


def colu(rez , file ,tn):
    #print(tn)
    with open(f'C:/Users/balaji Vyshnavy/Desktop/evidence/{file}', mode='a') as csv_file:
        fieldnames = rez
        writer = csv.DictWriter(csv_file, fieldnames=tn, )
        writer.writeheader()
        writer =csv.DictWriter(csv_file, fieldnames=fieldnames,)
        writer.writeheader()

def data(file,n):
    test_string=filter(n)
    test_string=int(test_string)
    #print(test_string)

    with open(f'C:/Users/balaji Vyshnavy/Desktop/evidence/{file}', mode='a') as csv_file:
        for i in range(0, test_string):
            pez = cur.fetchone()
            fieldnames = pez
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()


def filter(x):
    bad_chars = ['(', ')']
    bc = [',,']
    test_string = x
    test_string = str(test_string)
    for i in bad_chars:
        test_string = test_string.replace(i, '')
    for i in bc:
        test_string = test_string.replace(i, '')
    #print("Resultant list is : " + test_string)
    return test_string

def collect():
        shutil.copyfile('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.sql',
                    'C:/Users/Balaji Vyshnavy/Desktop/evidence/history.sql')
        shutil.copyfile('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.js',
                    'C:/Users/Balaji Vyshnavy/Desktop/evidence/history.js')
        shutil.copyfile('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.py',
                    'C:/Users/Balaji Vyshnavy/Desktop/evidence/history.py')
        shutil.copyfile('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/mysqlsh.log',
                    'C:/Users/Balaji Vyshnavy/Desktop/evidence/mysqlsh.log')
        shutil.copyfile('C:/ProgramData/MySQL/MySQL Server 8.0/Data/LAPTOP-67H7KN81.err',
                    'C:/Users/Balaji Vyshnavy/Desktop/evidence/LAPTOP-67H7KN81.err')
        shutil.copyfile('C:/ProgramData/MySQL/MySQL Server 8.0/Data/LAPTOP-67H7KN81-slow.log',
                    'C:/Users/Balaji Vyshnavy/Desktop/evidence/LAPTOP-67H7KN81-slow.log')
        shutil.copyfile('C:/ProgramData/MySQL/MySQL Server 8.0/Data/LAPTOP-67H7KN81.log',
                    'C:/Users/Balaji Vyshnavy/Desktop/evidence/LAPTOP-67H7KN81.log')

collect()

cur.execute('select column_name from information_schema.columns where table_name="user"')
rez=cur.fetchall()
tn="user"
colu(rez , 'user.csv',tn)
cur.execute('select count(*) from user')
n=cur.fetchall()
cur.execute('select * from user ')
data('user.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="innodb_table_stats"')
rez=cur.fetchall()
tn="innodb_table_stats"
colu(rez , 'innodb_table_stats.csv',tn)
cur.execute('select count(*) from innodb_table_stats')
n=cur.fetchall()
cur.execute('select * from innodb_table_stats ')
data('innodb_table_stats.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="tables_priv"')
rez=cur.fetchall()
tn="tables_priv"
colu(rez , 'tables_priv.csv',tn)
cur.execute('select count(*) from tables_priv')
n=cur.fetchall()
cur.execute('select * from tables_priv ')
data('tables_priv.csv',n)




cur.execute('use sys')
cur.execute('select column_name from information_schema.columns where table_name="user_summary"')
rez=cur.fetchall()
tn="user_summary"
colu(rez , 'user_summary.csv',tn)
cur.execute('select count(*) from user_summary')
n=cur.fetchall()
cur.execute('select * from user_summary ')
data('user_summary.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="host_summary"')
rez=cur.fetchall()
tn="host_summary"
colu(rez , 'host_summary.csv',tn)
cur.execute('select count(*) from host_summary')
n=cur.fetchall()
cur.execute('select * from host_summary ')
data('host_summary.csv',n)





cur.execute('use information_schema')
cur.execute('select column_name from information_schema.columns where table_name=" innodb_tablestats"')
rez=cur.fetchall()
tn="innodb_tablestats "
colu(rez , 'innodb_tablestats.csv',tn)
cur.execute('select count(*) from innodb_tablestats ')
n=cur.fetchall()
cur.execute('select * from innodb_tablestats')
data('innodb_tablestats.csv',n)
cur.execute('select column_name from information_schema.columns where table_name=" innodb_tables"')
rez=cur.fetchall()
tn="innodb_tables"
colu(rez , 'innodb_tables.csv',tn)
cur.execute('select count(*) from innodb_tables')
n=cur.fetchall()
cur.execute('select * from innodb_tables')
data('innodb_tables.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="files "')
rez=cur.fetchall()
tn="files"
colu(rez , 'files.csv',tn)
cur.execute('select count(*) from files')
n=cur.fetchall()
cur.execute('select * from files')
data('files.csv',n)
empty("columns.csv")
cur.execute('select column_name from information_schema.columns where table_name=" columns"')
rez=cur.fetchall()
tn="columns"
colu(rez , 'columns.csv',tn)
cur.execute('select count(*) from columns')
n=cur.fetchall()
cur.execute('select * from columns')
data('columns.csv',n)
empty("tables.csv")
cur.execute('select column_name from information_schema.columns where table_name=" tables"')
rez=cur.fetchall()
tn="tables"
colu(rez , 'tables.csv',tn)
cur.execute('select count(*) from tables')
n=cur.fetchall()
cur.execute('select * from tables')
data('tables.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="triggers "')
rez=cur.fetchall()
tn="triggers"
colu(rez , 'triggers.csv',tn)
cur.execute('select count(*) from triggers')
n=cur.fetchall()
cur.execute('select * from triggers')
data('triggers.csv',n)
cur.execute('select column_name from information_schema.columns where table_name=" views"')
rez=cur.fetchall()
tn="views"
colu(rez , 'views.csv',tn)
cur.execute('select count(*) from views')
n=cur.fetchall()
cur.execute('select * from views')
data('views.csv',n)
cur.execute('select column_name from information_schema.columns where table_name=" user_privileges"')
rez=cur.fetchall()
tn="user_privileges"
colu(rez , 'user_privileges.csv',tn)
cur.execute('select count(*) from user_privileges')
n=cur.fetchall()
cur.execute('select * from user_privileges')
data('user_privileges.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="table_privileges "')
rez=cur.fetchall()
tn="table_privileges"
colu(rez , 'table_privileges.csv',tn)
cur.execute('select count(*) from table_privileges')
n=cur.fetchall()
cur.execute('select * from table_privileges')
data('table_privileges.csv',n)



conn.close()