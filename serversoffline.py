#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:36:33 2020

@author: jean
"""



servers = [ [0,0,0,0,0] , [0,0,0,1,0] , [0,0,0,0,0] , [0,0,0,0,0] , [0,1,0,0,0] ]

#print( [ server for server in servers for server in server ] )
# print(servers)

def neighbours(i,j,tami,tamj):        
    ri = range( max( 0 ,  i-1 ) , min( i+2, tami ) )
    rj = range( max( 0 ,  j-1 ) , min( j+2, tamj ) )
    return [ (i,j) for i in ri for j in rj ]

def inc(matrix):
    online = [ ( i,j) for i in range(len(servers)) for j in range(len(servers[i])) if servers[i][j]==1]
    for i,j in online:
        neighboursServers = neighbours(i,j,len(servers),len(servers[i]))
        print(neighboursServers)
        for k,l in neighboursServers:
            servers[k][l] = 1
                
i = 0 
while 0 in [ server for server in servers for server in server ] and i < 5:
    print( [ server for server in servers for server in server ] )
    inc(servers)
    i += 1
    
    
print(i)
print( [ server for server in servers for server in server ] )
    