#!/usr/bin/python
import MySQLdb

"Connect to given database. Returns cursor."
def connect_db(dbname):
	db = MySQLdb.connect(host="localhost", 
                             user="root", 
        	             passwd="foobar1", 
	                     db=dbname) 

	return db.cursor()
