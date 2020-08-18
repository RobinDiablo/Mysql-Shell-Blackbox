import pymysql
import csv
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

hostname = 'localhost'
username = 'root'
password = 'rootpassword'
database = 'custom1'

conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
cur = conn.cursor()


def command_gen(rez):
    bad_chars = ['(', ')', "'"]
    test_string = rez[0]
    test_string = str(test_string)
    #for i in bad_chars:
    #    test_string = test_string.replace(i, '')
    #test_string = test_string.replace(',', '')
    #cmd1='use '+ pez
    cmd2='checksum table '+ test_string
    #print(cmd1)
    return cmd2
def db_gen(rez):
    test_string = rez[1]
    test_string = str(test_string)
    cmd1='use '+ test_string
    return cmd1

#with open(f'C:/Users/balaji Vyshnavy/Desktop/evidence/checksum.csv', mode='a') as f:
    #f.truncate()
    #f.close()


def writecsv(hash):
    with open(f'C:/Users/balaji Vyshnavy/Desktop/evidence/checksum.csv', mode='a') as csv_file:
        fieldnames = hash
        writer = csv.DictWriter(csv_file, fieldnames=hash, )
        writer.writeheader()

cur.execute('select table_name,table_schema from information_schema.tables')
gg=cur.fetchall()
for res in gg:
    cmd2 = command_gen(res)
    cmd1 = db_gen(res)
    #print(cmd1)
    #print(cmd2)
    cur.execute(cmd1)
    cur.execute(cmd2)
    hsh = cur.fetchall()
    print(hsh)
    #writecsv(hsh)

conn.close()






















#cmd=command_gen()
#cur.execute('use sys')
#cur.execute(cmd)
#cur.execute('select * from HASH')
#rez=cur.fetchall()
#print(rez)

#conn.commit()

'''def hash_table():
    #cur.execute("SET group_concat_max_len = 18446744073709547520")
    cur.execute("SELECT MD5( GROUP_CONCAT( CONCAT_WS('',timestamp,columns_csv,history_sql,LAPTOP_67H7KN81_LOG,tables_csv) SEPARATOR ',' ) ) as 'HASH SIGNATURE OF TABLE {HASH}' FROM hash")
    rez=cur.fetchall()
    print(rez)'''

#hash_table()
