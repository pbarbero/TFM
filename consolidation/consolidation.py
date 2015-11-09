#!/usr/bin/python
from position import Position

"Consolidation by time. Deletes positions too close by time."
def ConsolidationByTime(listPositions, lapse):
	i = 0
	result = []
	while i < len(listPositions) - 1:
		if not listPositions[i].is_neighboorhoudByTime(listPositions[i+1], lapse):
			result.append(listPositions[i])
		i=i+1
	#Por defecto anadiremos la ultima posicion, ya que no tiene siguiente con quien comparar
	result.append(listPositions[len(listPositions) - 1])
	
	return result
	

"Consolidation By distance. Usage: consolidationByDistance(listOfPositionsToConsolidate, epsilonToSetTheRadio, radius)"	
def ConsolidationByDistance(listPositions, eps, typeOfDistance):
	i = 0
	result = []
	while i < len(listPositions) - 1:
		# Distance EU simple
		if typeOfDistance == 0:
			if not listPositions[i].is_in_neighborhoodByEUSimple(listPositions[i+1], eps):
				result.append(listPositions[i])
		# Distance EU relative to speed
		elif typeOfDistance == 1:
			if not listPositions[i].is_in_neighborhoodByEURelativeSpeed(listPositions[i+1], eps):
				result.append(listPositions[i])
		# Distance EU relative to speed and orientation
		elif typeOfDistance == 2:
			if not listPositions[i].is_in_neighborhoodByEURelativeSpeedOrientation(listPositions[i+1], eps):
				result.append(listPositions[i])
		else:
			raise ValueError('That distance does not exist')
		i=i+1
			
	#Por defecto anadiremos la ultima posicion, ya que no tiene siguiente con quien comparar
	result.append(listPositions[len(listPositions) - 1])
	
	return result

"Deletes one position every k positions."
def ConsolidationEachNumber(listPositions, k):
	i = 0
	result = []
	while i < len(listPositions) - 1:
		if i%k == 0:
			result.append(listPositions[i])
		i = i+1

	return result
