# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 13:45:57 2017

@author: Luca
"""
import numpy as np

fname='geo3D.msh' #input filename
outname='geo3D.msh' #output filename

def read_NODES(name_mesh):
 file_grid=name_mesh
 read_nodes=0
 nodes={} # initialize dictionary, to have lookup function later
#-----------------
#with best implementation of reading a file, so python garbage collector will 
#-for sure- close the open file before opening another file (another with command)
#-----------------
 with open(file_grid, 'r') as grid: # 'r' = read 'rU' read UNIVERSAL EOL  
    grid.seek(0) #goes to the beginning of file, useful if need to iterate multiple times over the file
    for line in grid:
       if read_nodes==2: # first nodes line was the number of nodes, skip
        if '$EndNodes' not in line:    
           # read line as name (dict key) id_node, xyz pos
             line_s=line.split(' ')
             id_node=int(line_s[0])
             pos=(float(line_s[1]),float(line_s[2]),float(line_s[3]))
           # build dictionary element
             node_elem=(id_node,pos)
             nodes[id_node]=node_elem
        else:  
             read_nodes=0
       if read_nodes==1: # first nodes line is the number of nodes, read and skip
          read_nodes=2
       if '$Nodes' in line:    
          read_nodes=1
 return nodes

def create_new_MESH(name_mesh, nnodes):
 file_grid=name_mesh
 read_nodes=0
 out_mesh=''
#-----------------
#with best implementation of reading a file, so python garbage collector will 
#-for sure- close the open file before opening another file (another with command)
#-----------------
 with open(file_grid, 'r') as grid: # 'r' = read 'rU' read UNIVERSAL EOL  
    grid.seek(0) #goes to the beginning of file, useful if need to iterate multiple times over the file
    for line in grid:
       out=line 
       if read_nodes==2: # first nodes line was the number of nodes, skip
        if '$EndNodes' not in line:
             line_s=line.split(' ')
             id_node=int(line_s[0])
             out=str(nnodes[id_node][0])+' '+str(nnodes[id_node][1][0])+' '+str(nnodes[id_node][1][1])+' '+str(nnodes[id_node][1][2])+'\n'
        else:  
             read_nodes=0
       if read_nodes==1: # first nodes line is the number of nodes, read and skip
          read_nodes=2
       if '$Nodes' in line:    
          read_nodes=1
       out_mesh=out_mesh+out
 return out_mesh

nodes=read_NODES(fname)
new_nodes={}
new_z = {
0.0000000000000000 : 0.0000000000000000,
-0.8333333333333333 : -0.0458621757848043,
-1.666666666666667 : -0.1031898955158098,
-2.5000000000000000 : -0.1748495451795665,
-3.333333333333333 : -0.2644241072592625,
-4.1666666666666670 : -0.3763923098588824,
-5.0000000000000000 : -0.5163525631084074,
-5.833333333333333 : -0.6913028796703136,
-6.666666666666666 : -0.9099907753726963,
-7.5000000000000000 : -1.1833506450006748,
-8.3333333333333339 : -1.5250504820356479,
-9.1666666666666679 : -1.9521752783293642,
-10.000000000000000 : -2.4860812736965094,
-10.83333333333333 : -3.1534637679054409,
-11.66666666666667 : -3.9876918856666057,
-12.500000000000000 : -5.0304770328680615,
-13.33333333333333 : -6.3339584668698814,
-14.16666666666667 : -7.9633102593721556,
-15.000000000000000 : -10.000000000000000,

} # dictionary to define new x refined around well
for i in nodes:
    id_node=int(nodes[i][0])
    pos_z=new_z[nodes[i][1][2]]
    pos=(nodes[i][1][0],nodes[i][1][1],pos_z)
    node_elem=(id_node,pos)
    new_nodes[id_node]=node_elem

out=create_new_MESH(fname,new_nodes)    
"""
read_nodes=0
out_mesh=''
with open(fname, 'r') as grid: # 'r' = read 'rU' read UNIVERSAL EOL  
    grid.seek(0) #goes to the beginning of file, useful if need to iterate multiple times over the file
    for line in grid:
       out=line 
       if read_nodes==2: # first nodes line was the number of nodes, skip
        if '$EndNodes' not in line:
             line_s=line.split(' ')
             id_node=int(line_s[0])
             out=str(new_nodes[id_node][0])+' '+str(new_nodes[id_node][1][0])+' '+str(new_nodes[id_node][1][1])+' '+str(new_nodes[id_node][1][2])
        else:  
             read_nodes=0
       if read_nodes==1: # first nodes line is the number of nodes, read and skip
          read_nodes=2
       if '$Nodes' in line:    
          read_nodes=1
       print line   
       out_mesh=out_mesh+'\n'+out
"""
f = open(outname, 'w') # 'r' = read
f.write(out)
f.close()
