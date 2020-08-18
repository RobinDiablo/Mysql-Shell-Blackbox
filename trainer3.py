import csv


badw = ['GRANT PROXY ON','root@localhost on mysql using TCP/IP' ,'@is_mysql_encryopted' , 'DROP PREPARE stmt','SHOW FULL COLUMNS FROM','show columns from',' EXECUTE stmt','PREPARE stmt FROM @str','   DROP PREPARE stmt','   DROP PREPARE stmt ',' create table if not exsts  ','rollback','CREATE TABLE IF NOT EXISTS',' oracle ','@cmd','SHOW GLOBAL STATUS','GRANT SELECT ON']
with open('C:/ProgramData/MySQL/MySQL Server 8.0/Data/LAPTOP-67H7KN81.log', 'r+') as oldfile, open('C:/Users/Balaji Vyshnavy/Desktop/filter.txt', 'w+') as newfile:
    for line in oldfile:
        line.lstrip()
        if not any(bw in line for bw in badw) and line[0].isdigit():
                newfile.write(line)

oldfile.close()
newfile.close()
nf = open('C:/Users/Balaji Vyshnavy/Desktop/filter.txt', 'r+')
csvf = open('C:/Users/Balaji Vyshnavy/Desktop/filter.csv','w',newline='\n')
count = 0
bwl = ['USE mysql;',
       'FLUSH PRIVILEGES','flush privileges'
       'log_output',
       'mysql.user',
       'USE sys',
       'USE information_scehma',
       'security_admin', '@%', 'use information_scehma', 'use sys', 'use mysql',
       'history', 'GRANT', 'connect', 'delete', 'drop', 'create role', 'revoke', 'show privileges',
       'root@localhost', 'security_admin@localhost', 'security_admin@localhost on  using SSL/TLS'
       "use `sys`", "use `mysql", "use 'information_schema'", 'alter', 'ALTER',
       'select * into outfile',
       'oufile',
       'OUTFILE',
       'mysql',
       'information_schema.tables','information_schema','performance_schema','general_log']

def conclude(line):
    line.lstrip()
    if not any(bw in line for bw in bwl):
        return 0
    else:
        return 1


while True:
    count += 1
    line = nf.readline()
    c=conclude(line)
    c=str(c)
    l = line +c
    elements = l.strip().split('\n')
    print(elements)
    if not line:
        break
    #csvf.writelines(elements)
    writer = csv.DictWriter(csvf, fieldnames=elements)
    writer.writeheader()




