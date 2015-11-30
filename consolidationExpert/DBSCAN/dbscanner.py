'''
Created on Feb 13, 2014

@author: sushant
'''

from cluster import *
from pylab import *
from position import Position
from algorithms.db import connect_db

class dbscanner:
    
    dataSet = []
    count = 0
    visited = []
    member = []
    Clusters = []
    
    def dbscan(self,D,eps,MinPts):
        self.dataSet = D
        
        title(r'DBSCAN Algorithm', fontsize=18)
        xlabel(r'Dim 1',fontsize=17)
        ylabel(r'Dim 2', fontsize=17)
	plt.figure(figsize=(15,10))
        
        C = -1
        Noise = cluster('Noise')
        numit = 0
        for point in D:
            if point not in self.visited:
                self.visited.append(point)
                NeighbourPoints = self.regionQuery(point,eps)
                
                if len(NeighbourPoints) < MinPts:
                    Noise.addPoint(point)
                else:
                    name = 'Cluster'+str(self.count);
                    C = cluster(name)
                    self.count+=1;
                    self.expandCluster(point,NeighbourPoints,C,eps,MinPts)
                    
                    plot(C.getX(),C.getY(),'o',label=name)
                    hold(True)
		numit = numit +1

	print "NUMERO DE ITERACIONES"
	print numit
        
        if len(Noise.getPoints())!=0:
            plot(Noise.getX(),Noise.getY(),'x',label='Noise')
            
        hold(False)
        legend(loc='lower left')
        grid(True)
        show()
                    
                    
            
    
    def expandCluster(self,point,NeighbourPoints,C,eps,MinPts):
        
        C.addPoint(point)
        
        for p in NeighbourPoints:
            if p not in self.visited:
                self.visited.append(p)
                np = self.regionQuery(p,eps)
                if len(np) >= MinPts:
                    for n in np:
                        if n not in NeighbourPoints:
                            NeighbourPoints.append(n)
                    
            for c in self.Clusters:
                if not c.has(p):
                    if not C.has(p):
                        C.addPoint(p)
                        
            if len(self.Clusters) == 0:
                if not C.has(p):
                    C.addPoint(p)
                        
        self.Clusters.append(C)
        
        #C.printPoints()
        
                    
                
                     
    def regionQuery(self,P,eps):
#        result = []
#        for d in self.dataSet:
#            if (((d[0]-P[0])**2 + (d[1] - P[1])**2)**0.5)<=eps:
#                result.append(d)
#        return result
	# connect db
	cur = connect_db("bahia")
	consult = "SELECT id, recurso, latitud, longitud, velocidad, orientacion, UNIX_TIMESTAMP(fecha) FROM posicionesgps WHERE latitud = {0} AND longitud={1};"
	cmd = consult.format(P[1], P[0])
	print cmd
	cur.execute(cmd)
	
        pos = cur.fetchall()[0]
	P = Position(pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6])
	
	for d in self.dataSet:
	     cmd = consult.format(d.getX(), d.getY())
	     cur.execute(cmd)
	     pos = cur.fetchall()[0]
	     d = Position(pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6])
	     if d.is_in_neighborhoodByEURelativeSpeed(P, 0.001):
		result.append(d)
	return result

    
            
            
            
        
                
                 
            
            
            
            
        
