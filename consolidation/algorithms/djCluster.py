from position import Position, Cluster

"Dj-Clustering Algorithm"
def DjCluster(setPoints, typeDistance, eps, minPoints, t0):

	# Lista clusters
	listClusters = []
	# Puntos ruido
	listNoises = []

	# Para todos los puntos del set
	for p in setPoints:
		# Calculamos el vecindario N(p) y el minimo de puntos indicado
		np = computeNeighborhood(p, setPoints, typeDistance, minPoints, eps, t0)

		# DEBUG
		if np is not None:
			print np.toString()

		# Si N(p) es nulo (es decir, N(p) no esta en un cluster)
		if np is None:
			listNoises.append(p) # etiquetamos el punto como ruido
		else:
			# Calculamos si np es density joinable con alguno de la lista
			result = np.isDensityJoinable(listClusters)

			if result is None:
				listClusters.append(np) # creamos un nuevo cluster
			else:
				result.mergeCluster(np)

	return [listClusters, listNoises]

"Compute Neighborhood"
def computeNeighborhood(p, setPoints, typeDistance, minPoints, eps, t0):
	pointsOfCluster = []
	for q in setPoints:
		if typeDistance == 0:
			if p.is_in_neighborhoodByEUSimple(q, eps):
				pointsOfCluster.append(q)
		elif typeDistance == 1:
			if p.is_in_neighborhoodEURelativeSpeed(q, eps):
				pointsOfCluster.append(q)
		elif typeDistance == 2:
			if p.is_in_neighborhoodT0Reachable(q, t0):
				pointsOfCluster.append(q)

	if len(pointsOfCluster) < minPoints:
		return None
	else:
		return Cluster(p, pointsOfCluster)

	
	
			
