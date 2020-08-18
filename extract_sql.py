import pymysql
import os

hostname = 'localhost'
username = 'root'
password = 'rootpassword'
database = 'custom1'

conn = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
cur = conn.cursor()

if os.path.isfile('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/user_summary.csv')==False:

	cur.execute("use sys;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/user_summary.csv' fields terminated by ',' from user_summary ;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/host_summary.csv' fields terminated by ',' from host_summary;")


	cur.execute("use mysql;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/innodb_table_stats.csv' fields terminated by ',' from innodb_table_stats ;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tables_priv.csv' fields terminated by ',' from tables_priv;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/user.csv' fields terminated by ',' from user;")

	cur.execute("use information_schema;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/columns.csv' fields terminated by ',' from columns;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/files.csv' fields terminated by ',' from files;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/innodb_tables.csv' fields terminated by ',' from innodb_tables;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/innodb_tablestats.csv' fields terminated by ',' from innodb_tablestats;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tables.csv' fields terminated by ',' from tables;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/triggers.csv' fields terminated by ',' from triggers;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/views.csv' fields terminated by ',' from views;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/user_privileges.csv' fields terminated by ',' from user_privileges;")
	cur.execute("select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/table_privileges.csv' fields terminated by ',' from table_privileges;")

conn.close()