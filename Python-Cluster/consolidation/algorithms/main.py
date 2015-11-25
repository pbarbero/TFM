#!/usr/bin/python
#from consolidation import consolidationByDistance, consolidationByTime, consolidationEachNumber
import consolidation
from position import Position
from datetime import datetime
from db import connect_db 
from djCluster import DjCluster

def main():
#	eps = 0.1
#	p = Position("id", "recurso", -0.22707989811897278, -0.6720935106277466, 0, 112, "2015-02-17 08:00:06")
#	q = Position("id", "recurso", -0.22707989811897278, -0.6720935106277466, 0, 112, "2015-02-17 08:00:06")
#	print p.is_neighboorhoud(q, eps)

	cur_sal = connect_db("posicionesSalvador")
	cur_rio = connect_db("posicionesRio")

	logFile = "simpleConsolidation.log"
	limit = 10
	cmd = "SELECT * FROM posicionesgps LIMIT {0};".format(limit)
	cur_sal.execute(cmd)

	list_pos = []

	for row in cur_sal.fetchall():
		q = Position(row[0]
			   , row[2]
			   , row[3]
			   , row[4]
			   , row[5]
			   , row[6]
			   , row[10]
		            )
		list_pos.append(q)

	# Consolidations
	#result = consolidationByDistance(list_pos, 0.5)
	#result = consolidationEachNumber(list_pos, 2)
	#result = consolidationByTime(list_pos, 1)
	result = consolidation.ConsolidationByDistance(list_pos, 2, 0, 1)

#	print "EPIS LIST: Result -> " + str(len(result)) + " positions."
#	for pos in result:
#		print pos.toString()

	# CLUSTERING
	#print "CLUSTERING"
	#print DjCluster(list_pos, 0, 0.5, 2, 0.50)
	


if __name__ == '__main__':
	main()
