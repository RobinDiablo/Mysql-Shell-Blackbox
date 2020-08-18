import csv

logf = open('C:/Users/Balaji Vyshnavy/AppData/Roaming/MySQL/mysqlsh/history.sql', 'r+')
nf=open('C:/Users/Balaji Vyshnavy/Desktop/history.csv','w+',newline='\n')
#data = [row for row in csv.reader(nf)]
#print(data[1][1])

count = 0
bwl = ['GRANT','delete','drop','create role','revoke','show privileges','%@localhost','#'
       'root@localhost','security_admin','%@%','use information_scehma','use sys','use mysql','sys',
       'information_schema.tables','information_schema','output','log_output','performance_schema',
       'general_log',
        '\history clear','\option logLevel','\option verbose','\option logLevel=','logLevel'
        '\option history.autosave=0'
        ,'\option verbose','\option verbose=','\option --persist logLevel=','verbose'
        ,'\option --persist verbose=','\option --persist logLevel','\option --persist verbose'
        '\option history.autoSave=false',
        '\option history.autosave 0','\option history.autosave=0'
        '\option history.autoSave false',
        '\option --persist history.autoSave=false',
        '\option --persist history.autosave 0','\option --persist history.autosave=0'
        '\option --persist history.autoSave false',
        '\option --persist history.autosave=0'
           ,'\option history.autoSave=0','\history autoSave=0',
        '\option --persist history.autoSave=false',
        '\option history.maxSize=','--persist'
        '\option --persist history.maxSize=',
        '\option --persist history.maxSize',
        '\history clear',
        '\history delete','\option --persist '
        '\connect root@localhost:3306',
        '\connect security_admin@localhost:3306',
        'connect security_admin',
        '\connect root',
        '\option --persist defaultMode',]


def conclude(line):
    line.lstrip()
    if not any(bw in line for bw in bwl):
        return 0
    else:
        return 1

while True:
    count += 1
    line = logf.readline()
    c=conclude(line)
    c=str(c)
    l = line +c

    elements = l.strip().split('\n')
    print(elements)
    if not line:
        break
    #nf.writelines(l)
    writer = csv.DictWriter(nf, fieldnames=elements)
    writer.writeheader()


