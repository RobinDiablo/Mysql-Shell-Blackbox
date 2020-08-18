
import csv
import pymysql


hostname = 'localhost'
username = 'root'
password = 'rootpassword'
database = 'mysql'

conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
cur = conn.cursor()


def colu(rez , file ,tn):
    tn=tuple(tn)
    with open(f'C:/Users/balaji Vyshnavy/Desktop/evidence/{file}', mode='w') as csv_file:
        fieldnames = rez
        writer = csv.DictWriter(csv_file, fieldnames=tn, )
        writer.writeheader()
        writer =csv.DictWriter(csv_file, fieldnames=fieldnames,)
        writer.writeheader()

def data(file,n):
    test_string=filter(n)
    test_string=int(test_string)

    with open(f'C:/Users/balaji Vyshnavy/Desktop/{file}', mode='w') as csv_file:
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
    return test_string

cur.execute('select column_name from information_schema.columns where table_name="user"')
rez=cur.fetchall()
tn="user"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from user')
n=cur.fetchall()
cur.execute('select * from user ')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="innodb_table_stats"')
rez=cur.fetchall()
tn="innodb_table_stats"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from innodb_table_stats')
n=cur.fetchall()
cur.execute('select * from innodb_table_stats ')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="tables_priv"')
rez=cur.fetchall()
tn="tables_priv"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from tables_priv')
n=cur.fetchall()
cur.execute('select * from tables_priv ')
data('test.csv',n)




cur.execute('use sys')
cur.execute('select column_name from information_schema.columns where table_name="user_summary"')
rez=cur.fetchall()
tn="user_summary"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from user_summary')
n=cur.fetchall()
cur.execute('select * from user_summary ')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="host_summary"')
rez=cur.fetchall()
tn="host_summary"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from host_summary')
n=cur.fetchall()
cur.execute('select * from host_summary ')
data('test.csv',n)





cur.execute('use information_schema')
cur.execute('select column_name from information_schema.columns where table_name=" innodb_tablestats"')
rez=cur.fetchall()
tn="innodb_tablestats "
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from innodb_tablestats ')
n=cur.fetchall()
cur.execute('select * from innodb_tablestats')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name=" innodb_tables"')
rez=cur.fetchall()
tn="innodb_tables"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from innodb_tables')
n=cur.fetchall()
cur.execute('select * from innodb_tables')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="files "')
rez=cur.fetchall()
tn="files"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from files')
n=cur.fetchall()
cur.execute('select * from files')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name=" columns"')
rez=cur.fetchall()
tn="columns"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from columns')
n=cur.fetchall()
cur.execute('select * from columns')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name=" tables"')
rez=cur.fetchall()
tn="tables"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from tables')
n=cur.fetchall()
cur.execute('select * from tables')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="triggers "')
rez=cur.fetchall()
tn="triggers"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from triggers')
n=cur.fetchall()
cur.execute('select * from triggers')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name=" views"')
rez=cur.fetchall()
tn="views"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from views')
n=cur.fetchall()
cur.execute('select * from views')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name=" user_privileges"')
rez=cur.fetchall()
tn="user_privileges"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from user_privileges')
n=cur.fetchall()
cur.execute('select * from user_privileges')
data('test.csv',n)
cur.execute('select column_name from information_schema.columns where table_name="table_privileges "')
rez=cur.fetchall()
tn="table_privileges"
colu(rez , 'test.csv',tn)
cur.execute('select count(*) from table_privileges')
n=cur.fetchall()
cur.execute('select * from table_privileges')
data('test.csv',n)



conn.close()