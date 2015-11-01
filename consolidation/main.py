#!/usr/bin/python
from position import Position
from datetime import datetime
from db import connect_db 

def main():
	eps = 0.1
	p = Position("id", "recurso", -0.22707989811897278, -0.6720935106277466, 0, 112, "2015-02-17 08:00:06")
	q = Position("id", "recurso", -0.22707989811897278, -0.6720935106277466, 0, 112, "2015-02-17 08:00:06")
	print p.is_neighboorhoud(q, eps)

	cur_sal = connect_db("posicionesSalvador")
	cur_rio = connect_db("posicionesRio")

	limit = 5000000 
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

	print len(list_pos)


if __name__ == '__main__':
	main()
