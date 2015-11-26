'''
Created on Feb 13, 2014

@author: sushant
'''

from dbscanner import *
import csv
import re

#configPath = '/home/sushant/config'
#dataPath = '/home/sushant/abc.csv'
configPath = 'config'
dataPath = 'abc.csv'

def main():
    [Data,eps,MinPts]= getData()
    dbc= dbscanner()
    print "eps is {0}".format(eps)
    print "MinPts is {0}".format(MinPts)
    print "Howmany is {0}".format(len(Data))
    dbc.dbscan(Data, eps, MinPts)
    
def getData():
    Data = []

    with open(dataPath,'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            #row = re.split(r'\t+',row[0])
            Data.append([float(row[0]),float(row[1])])

    f = open(configPath,'r')
    
    [eps,MinPts] = parse(f.readline())
    
    return [Data,eps,MinPts]

def parse(line):
    data = line.split(" ")
    return [int(data[0]),int(data[1])]
    
            
    
main()    
