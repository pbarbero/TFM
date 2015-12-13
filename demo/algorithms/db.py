import MySQLdb
from position import Position
import numpy as np

"Connect to given database. Returns cursor."
def connect_db(dbname):
	db = MySQLdb.connect(host="localhost", 
                             user="root", 
        	             passwd="foobar1", 
	                     db=dbname) 

	return db.cursor()

"Return list of positions"
def getPositions(dbname, cmd, recurso, limit):
	cur = connect_db(dbname)
	cur.execute(cmd.format(recurso,limit))

	list_pos = []

	for q in cur.fetchall():
		p = Position(q[0], q[1], q[2], q[3], q[4], q[5], q[6])	
		list_pos.append(p)

	return list_pos


"Normalizes a list of positions"
def normalize(list_pos):
        listPosTyp = []
	lats = []
	longs = []
	times = []

        # Calculamos media lat
	for pos in list_pos:
		lats.append(pos.lat)
		longs.append(pos.lon)
		times.append(pos.date)

        # Calculamos las medias 
        meanLat = np.mean(lats)
        meanLon = np.mean(longs)
	meanTime = np.mean(times)

        # Calculamos desv 
        devLat = np.std(lats)
        devLon = np.std(longs)
	devTimes = np.std(times)

        latsTyp = []
        longsTyp = []

        for pos in list_pos:
                q = Position(pos.id
                           , pos.resource
                           , (pos.lat - meanLat)/devLat
                           , (pos.lon - meanLon)/devLon
                           , pos.speed
                           , pos.track
                           , (pos.date - meanTime)/devTimes
                           )
                listPosTyp.append(q)
                latsTyp.append(q.lat)
                longsTyp.append(q.lon)

	return [listPosTyp, latsTyp, longsTyp]

"Delete positions"
def deletePositions(dbname, list_pos):
	cur = connect_db(dbname)
	for pos in list_pos:
		cmd = "DELETE FROM posicionesgps WHERE id={0}".format(pos.id)
		cur.execute(cmd)
		print "{0} deleted!".format(pos.toString())
