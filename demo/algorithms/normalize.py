import numpy as np
from position import Position

"Normalizes a list of positions"
def normal(list_pos):
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
