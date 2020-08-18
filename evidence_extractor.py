import csv
import shutil
import os
from openpyxl import load_workbook
from datetime import timedelta,datetime



dateTimeObj=datetime.utcnow()
cal={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
m=dateTimeObj.strftime("%b")
for x, y in cal.items():
  if m==x:
    m=y
time=dateTimeObj.strftime("%Y-")+str(m)+dateTimeObj.strftime("-%dT%H:%M:%S.%f")



wb = load_workbook(r'C:\Users\Balaji Vyshnavy\Desktop\state2.xlsx')
sheet = wb.active
  

badw = ['GRANT PROXY ON','root@localhost on mysql using TCP/IP' ,'@is_mysql_encryopted' ,'@@' ,'DROP PREPARE stmt','SHOW FULL COLUMNS FROM','show columns from',' EXECUTE stmt','PREPARE stmt FROM @str','   DROP PREPARE stmt','   DROP PREPARE stmt ',' create table if not exsts  ','rollback','CREATE TABLE IF NOT EXISTS',' oracle ','@cmd','SHOW GLOBAL STATUS','GRANT SELECT ON']
with open('C:/ProgramData/MySQL/MySQL Server 8.0/Data/LAPTOP-67H7KN81.log', 'r') as oldfile, open('C:/Users/Balaji Vyshnavy/Desktop/logs/temp.txt', 'w+') as newfile:
    for line in oldfile:
        line.lstrip()
        if not any(bw in line for bw in badw) and line[0].isdigit():
                newfile.write(line)

oldfile.close()
newfile.close()


def search_index(time,data,l):
  i=0
  while i<l:
    t=res[i]
    t=t[0:16]
    i=i+1
    if t==time:
      return i
  return 0


trunc=open('C:/Users/Balaji Vyshnavy/Desktop/logs/evidence.csv', 'a')
trunc.truncate()
trunc.close()
temp=open('C:/Users/Balaji Vyshnavy/Desktop/logs/temp.txt', 'r+')
res=temp.readlines()
len=len(res)
t=res[len-1]
t=t[0:16]
print(t)
s=sheet['B1'].value
s=s[0:16]
print(s)
cursor=search_index(s,res,len)
save=open('C:/Users/Balaji Vyshnavy/Desktop/logs/evidence.csv', 'a')
print("Total new records:",len-cursor)
while cursor<len:
  save.write(res[cursor])
  cursor=cursor+1



if os.path.isfile('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.sql')==True and  os.path.isfile('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.sql')==False:
  shutil.move('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.sql','C:/Users/Balaji Vyshnavy/Desktop/logs/temp/')
if os.path.isfile('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.js')==True and os.path.isfile('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.js')==False:
  shutil.move('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.js','C:/Users/Balaji Vyshnavy/Desktop/logs/temp/')
if os.path.isfile('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.py')==True and os.path.isfile('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.py')==False:
  shutil.move('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.py','C:/Users/Balaji Vyshnavy/Desktop/logs/temp/')

def append(file1,file2,time):
  with open(file1, 'r') as oldfile, open(file2, 'w') as newfile:
    newfile.write(time)
    for line in oldfile:
        line.lstrip()
        newfile.write(line)


append('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.sql','C:/Users/Balaji Vyshnavy/Desktop/logs/locker/history.sql',time)
append('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.py','C:/Users/Balaji Vyshnavy/Desktop/logs/locker/history.py',time)
append('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.js','C:/Users/Balaji Vyshnavy/Desktop/logs/locker/history.js',time)

def uploadevidence(file1,file2):
    with open(file1, 'r') as oldfile, open(file2, 'a') as newfile:
      for line in oldfile:
          line.lstrip()
          newfile.write(line)

uploadevidence('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.sql','C:/Users/Balaji Vyshnavy/Desktop/logs/evidence.csv')  
uploadevidence('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.js','C:/Users/Balaji Vyshnavy/Desktop/logs/evidence.csv')
uploadevidence('C:/Users/Balaji Vyshnavy/Desktop/logs/temp/history.py','C:/Users/Balaji Vyshnavy/Desktop/logs/evidence.csv')  


