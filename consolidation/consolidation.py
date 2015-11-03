#!/usr/bin/python
from position import Position


def consolidationByEps(listPositions, eps):
	i = 0;
	result = []
	while i < len(listPositions) - 1:
		if not listPositions[i].is_neighboorhoud(listPositions[i+1], eps):
			result.append(listPositions[i])
		i=i+1
	#Por defecto anadiremos la ultima posicion, ya que no tiene siguiente con quien comparar
	result.append(listPositions[len(listPositions) - 1])
	
	return result
