#!/usr/bin/python

import sys
from dbscanner import *
import numpy as np
from algorithms.db import connect_db


def main():
	if len(sys.argv) != 4:
		print 'Args: eps, minPts and how many data you want'
	else:
		eps=sys.argv[1]
		MinPts=sys.argv[2]
		limit = sys.argv[3]
		print "eps is {0}".format(eps)
		print "minPts is {0}".format(MinPts)
		print "howmany is {0}".format(limit)
		
		cur= connect_db("bahia")
		recurso = "tetra:12082781"
		cmd = "SELECT latitud, longitud FROM posicionesgps WHERE latitud <> 0 and longitud <> 0 and recurso=\"{0}\" ORDER BY fecha ASC LIMIT {1};".format(recurso, limit)
		cur.execute(cmd)

		a=[]
		for pos in cur.fetchall():
		    a.append([pos[0], pos[1]])

		Data = a

		dbc = dbscanner()
		dbc.dbscan(Data, eps, MinPts)
	
main()
