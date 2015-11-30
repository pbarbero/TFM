import numpy as np

"Normalizes a list of positions"
def normal(list_pos):
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

	return [listPosTyp, latsTyp, longsTyp]
