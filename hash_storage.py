import pymysql
import hashing
from datetime import datetime

hostname = 'localhost'
username = 'root'
password = 'rootpassword'
database = 'sys'



conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
cur = conn.cursor()

list=("C:/Users/Balaji Vyshnavy/Desktop/evidence/columns.csv"
      ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/history.sql"
      ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/LAPTOP-67H7KN81.log"
      ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/innodb_tables.csv")

def command_gen():
    dateTimeObj = datetime.now()
    time= dateTimeObj.strftime("%d-%b-%Y--%H:%M:%S.%f-")
    res=""
    for file in list:
        res=res +"','"+ hashing.custom_hash(file)
    res = "('" + time + res + "')"
    cmd="insert into HASH values"+res
    return cmd

#cmd=command_gen()
cur.execute('use sys')
#cur.execute(cmd)
cur.execute('select * from HASH')
rez=cur.fetchall()
print(rez)

conn.commit()

def hash_table():
    #cur.execute("SET group_concat_max_len = 18446744073709547520")
    cur.execute("SELECT MD5( GROUP_CONCAT( CONCAT_WS('',timestamp,columns_csv,history_sql,LAPTOP_67H7KN81_LOG,tables_csv) SEPARATOR ',' ) ) as 'HASH SIGNATURE OF TABLE {HASH}' FROM hash")
    rez=cur.fetchall()
    print(rez)

hash_table()
conn.close()



#g='select * from logininfo'
#cur.execute('use custom1')
#cur.execute(g)
#rez=cur.fetchall()
#print(rez)
#print(g)




'''cmd=command_gen()
print(cmd)
cur.execute('use sys')
cur.execute(cmd)
cur.execute('select * from HASH')
rez=cur.fetchall()
print(rez)'''



'''def command_gen():
    def file_as_bytes(file):
        with file:
            return file.read()
    print(hashlib.sha256(file_as_bytes(open("C:/Users/Balaji Vyshnavy/Desktop/evidence/files.csv", 'rb'))).hexdigest())
    res=hashlib.sha256(file_as_bytes(open("C:/Users/Balaji Vyshnavy/Desktop/evidence/files.csv", 'rb'))).hexdigest()
    #res=hashing.custom_hash()
    cmd="insert into hash values('"+res+"')"
    return cmd'''
