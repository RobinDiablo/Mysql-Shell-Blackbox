import pymysql

hostname = 'localhost'
username = 'root'
password = 'rootpassword'
database = 'custom1'

conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
cur = conn.cursor()


cur.execute("show grants for 'maintenance_admin'@'%'")
res=cur.fetchall()
res=str(res)
if res.find("maintenance")==-1:
	cur.execute("create role 'maintenance'")
	cur.execute("grant 'maintenance' to 'maintenance_admin'@'%'")
	cur.execute("GRANT SELECT, UPDATE, CREATE ,drop,delete,alter on loginginfo to 'maintenance'")

conn.commit()
conn.close()