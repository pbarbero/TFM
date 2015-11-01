from position import Position
from datetime import datetime


def main():
	eps = 0.1
	p = Position("id", "recurso", -0.22707989811897278, -0.6720935106277466, 0, 112, "2015-02-17 08:00:06")
	q = Position("id", "recurso", -0.22707989811897278, -0.6720935106277466, 0, 112, "2015-02-17 08:00:06")
	print p.is_neighboorhoud(q, eps)

if __name__ == '__main__':
	main()
