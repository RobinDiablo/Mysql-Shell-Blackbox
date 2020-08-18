bwl = ['GRANT PROXY ON', '@is_mysql_encryopted' , 'DROP PREPARE stmt','SHOW FULL COLUMNS FROM','show columns from',' EXECUTE stmt','PREPARE stmt FROM @str','   DROP PREPARE stmt','   DROP PREPARE stmt ',' create table if not exsts  ','rollback','CREATE TABLE IF NOT EXISTS',' oracle ','@cmd','SHOW GLOBAL STATUS','GRANT SELECT ON']
gwl = ['USE', 'INSERT','CREATE']
with open('C:/ProgramData/MySQL/MySQL Server 8.0/Data/LAPTOP-67H7KN81.log','r+') as oldfile, open('C:/Users/Balaji Vyshnavy/Desktop/filter.txt', 'w+') as newfile:
    for line in oldfile:
        line.lstrip()
        if not any(bw in line for bw in bwl) and line[0].isdigit():
                print(line)
                newfile.write(line)