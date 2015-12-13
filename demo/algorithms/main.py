#!/usr/bin/python
import consolidation as cs
from position import Position
from db import connect_db 
from normalize import normal
from djCluster import DjCluster

import matplotlib.pyplot as plt
from pylab import *
from datetime import datetime


def main():
	cur_sal = connect_db("posicionesSalvador")

	limit = 100
	cmd = "SELECT * FROM posicionesgps WHERE latitud<>0 AND longitud<> 0 AND recurso='tetra:12082781' LIMIT {0};".format(limit)
	cur_sal.execute(cmd)

	list_pos = []
	for row in cur_sal.fetchall():
		q = Position(row[0] # id
			   , row[2] # resource
			   , row[3] # lat
			   , row[4] # lon
			   , row[5] # speed
			   , row[6] # track
			   , row[10] # date
		            )
		list_pos.append(q)

	# Tipificar
	listPosTyp = []
        lats = []
        longs = []

        # Calculamos media lat
        for pos in list_pos:
                lats.append(pos.lat)
        meanLat = np.mean(lats)
        # Calculamos media lon 
        for pos in list_pos:
                longs.append(pos.lon)
        meanLon = np.mean(longs)
        # Calculamos desv lat
        devLat = np.std(lats)
        # Calculamos desv lon
        devLon = np.std(longs)

        latsTyp = []
        longsTyp = []
        for pos in list_pos:
                q = Position(pos.id
                           , pos.resource
                           , (pos.lat - meanLat)/devLat
                           , (pos.lon - meanLon)/devLon
                           , pos.speed
                           , pos.track
                           , pos.date
                           )
                listPosTyp.append(q)
                latsTyp.append(q.lat)
                longsTyp.append(q.lon)	

	# Consolidations
	result = cs.ConsolidationByDistance(list_pos, 0, 0.001, 1)
	#result = cs.ConsolidationByThinning(list_pos, 2, 5)
	#result = cs.ConsolidationByTime(list_pos, 1)

	# PLOT INIT DATA
	plt.figure(1)
	plt.subplot(211)
	plt.title(r'Data', fontsize=18)
        plt.xlabel(r'latitud',fontsize=17)
        plt.ylabel(r'longitud', fontsize=17)
	plt.grid(True)
        plt.figure(figsize=(20,30))
	plt.plot(latsTyp, longsTyp, 'ro')
	plt.show()

	# PLOT RESULTS
	latResult = []
	longsResult = []
	for pos in result:
		latResult.append(pos.lat)
		longsResult.append(pos.lon)

	plt.figure(1)
        plt.subplot(211)
        plt.title(r'DataResult', fontsize=18)
        plt.xlabel(r'latitud',fontsize=17)
        plt.ylabel(r'longitud', fontsize=17)
        plt.grid(True)
        plt.figure(figsize=(20,30))
        plt.plot(latResult, longsResult, 'bo')
        plt.show()

	# Results
	print "Numero de posiciones iniciales: {0}".format(str(len(list_pos)))
	print "Numero de posiciones finales: {0}".format(str(len(result)))


if __name__ == '__main__':
	main()
