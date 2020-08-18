import hashlib

def system_hash():
    def file_as_bytes(file):
        with file:
            return file.read()
    fnamelst=("C:/Users/Balaji Vyshnavy/Desktop/evidence/files.csv","C:/Users/Balaji Vyshnavy/Desktop/evidence/user.csv"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/innodb_tablestats.csv"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/innodb_table_stats.csv","C:/Users/Balaji Vyshnavy/Desktop/evidence/innodb_tables.csv"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/table_privileges.csv"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/host_summary.csv","C:/Users/Balaji Vyshnavy/Desktop/evidence/test.csv",
              "C:/Users/Balaji Vyshnavy/Desktop/evidence/triggers.csv"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/user_privileges.csv","C:/Users/Balaji Vyshnavy/Desktop/evidence/user_summary.csv"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/views.csv","C:/Users/Balaji Vyshnavy/Desktop/evidence/mysqlsh.log"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/history.js","C:/Users/Balaji Vyshnavy/Desktop/evidence/history.sql"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/LAPTOP-67H7KN81.err"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/LAPTOP-67H7KN81-slow.log"
              ,"C:/Users/Balaji Vyshnavy/Desktop/evidence/LAPTOP-67H7KN81.log"
              "C:/Users/Balaji Vyshnavy/Desktop/evidence/columns.csv")
    for fname in fnamelst:
        print(hashlib.sha256(file_as_bytes(open(fname, 'rb'))).hexdigest())



def custom_hash(file):
    def file_as_bytes(file):
        with file:
            return file.read()
    #print(hashlib.sha256(file_as_bytes(open(file, 'rb'))).hexdigest())
    return(hashlib.sha256(file_as_bytes(open(file, 'rb'))).hexdigest())

ert=custom_hash("C:/Users/Balaji Vyshnavy/Desktop/evidence/LAPTOP-67H7KN81.log")
#print(ert)


