#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random


# In[2]:


def output(P):
    for Chr in P:
        print('(',end='')
        for i in range(len(Chr)-1):
            print("%+d"%Chr[i],end = ' ')
        print('%+d)'%Chr[-1],end='')
    print()


# In[3]:


def TwoBreakOnGenomeGraph(GenomeGraph, i1 , i2 , i3 , i4):
     #remove colored edges (i1, i2) and (i3, i4) from GenomeGraph
    if (i1,i2) in GenomeGraph:
        GenomeGraph.remove((i1,i2))
    else:
        GenomeGraph.remove((i2,i1))
    if (i3,i4) in GenomeGraph:
        GenomeGraph.remove((i3,i4))
    else:
        GenomeGraph.remove((i4,i3))
     #add colored edges (i1, i3) and (i2, i4) to GenomeGraph
    GenomeGraph.append((i1,i3))
    GenomeGraph.append((i2,i4))
    return GenomeGraph


# In[4]:


def ChromosomeToCycle(Chromosome):
    n = len(Chromosome)
    Nodes = np.zeros(2*n)
    for j in range(n):
        i = Chromosome[j]
        if i > 0:
            Nodes[2*j] = int(2*i-1)
            Nodes[2*j+1]  =  int(2*i)
        else:
            Nodes[2*j]  = int(-2*i)
            Nodes[2*j+1]  =  int(-2*i-1)
    return Nodes


# In[5]:


def Distance(Edge):
    StartPoint = Edge[0][0]
    node_suf =  Edge[0][1]
    Edge.pop(0)
    Cycle_num = 0
    while(Edge):
        for i in range(len(Edge)):
            Node = Edge[i]
            if(Node[0] == node_suf):
                node_suf = Node[1]
                Edge.pop(i)
                break
            elif(Node[1] == node_suf):
                node_suf = Node[0]
                Edge.pop(i)
                break
                
        if(node_suf == StartPoint):
            if(not Edge):
                return Cycle_num +1
            Cycle_num += 1
            StartPoint = Edge[0][0]
            node_suf =  Edge[0][1]
            Edge.pop(0)
    return Cycle_num


# In[6]:


def ColoredEdges(P):
    Edges = []
    #for idx,Chromosome in P.items():
    for Chromosome in P:
        Nodes = ChromosomeToCycle(Chromosome)
        n = len(Chromosome)
        for j in range(n):
            if(j<n-1):
                Edges.append((int(Nodes[2*j+1]),int(Nodes[2*j+2])))
            else:
                Edges.append((int(Nodes[2*j+1]),int(Nodes[0])))
    return Edges


# In[310]:


def GraphToGenome(GenomeGraph):
    P = []
    StartPoint = GenomeGraph[0][0]
    node_suf = GenomeGraph[0][1]
    GenomeGraph.pop(0)
    Chr  = [StartPoint,node_suf]
    while(GenomeGraph):
        for i in range(len(GenomeGraph)):
            Node = GenomeGraph[i]
            if(Node[0]-pow(-1, Node[0]) == node_suf):
                Chr.append(Node[0])
                Chr.append(Node[1])
                node_suf = Node[1]
                GenomeGraph.pop(i)
                break
            elif(Node[1]-pow(-1,Node[1]) == node_suf):
                Chr.append(Node[1])
                Chr.append(Node[0])
                node_suf = Node[0]
                GenomeGraph.pop(i)
                break      
        if(node_suf-pow(-1,node_suf) == StartPoint):
            ele = Chr.pop(-1)
            Chr.insert(0,ele)
            Chromosome = CycleToChromosome(Chr)
            P.append(Chromosome)
            if(not GenomeGraph):
                return P
            StartPoint = GenomeGraph[0][0]
            node_suf =  GenomeGraph[0][1]
            GenomeGraph.pop(0)
            Chr = [StartPoint,node_suf] 
            if(not GenomeGraph):
                Chromosome = CycleToChromosome(Chr)
                P.append(Chromosome)
                return P                       
    return P


# In[8]:


def CycleToChromosome(Nodes): 
    n = int(len(Nodes)/2)
    Chromosome = np.zeros(n).astype(int)
    for j in range(n):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome[j] =  Nodes[2*j+1] /2
        else:
            Chromosome[j]  = -Nodes[2*j]/2
    return Chromosome


# In[311]:


def TwoBreakOnGenome(P, i1 , i2 , i3 , i4 ):
    Edge1 = ColoredEdges(P)
    GenomeGraph = TwoBreakOnGenomeGraph(Edge1, i1 , i2 , i3 , i4)
    P = GraphToGenome(GenomeGraph)
    return P


# In[10]:


def PreProcess(inp):
    Genome = []
    inp = np.array(inp.split(')'))
    for i in range(len(inp)-1):
        chrm = inp[i]
        chrm = chrm[1:]
        Genome.append(np.array(chrm.split(' ')).astype(int))
    return Genome


# In[351]:


def FindTrivalCycle(BlueEdges,RedEdges,i1,i2,i3,i4):
    RedEdges.remove((i1,i2))
    RedEdges.remove((i3,i4))
    Total_count = 0
    if (i1,i3) in BlueEdges:
        RedEdges.append((i2,i4))
        BlueEdges.remove((i1,i3))
        Total_count += 1
    elif (i3,i1) in BlueEdges:
        RedEdges.append((i2,i4))
        BlueEdges.remove((i3,i1))
        Total_count += 1
    if (i2,i4) in BlueEdges:
        RedEdges.append((i1,i3))
        BlueEdges.remove((i2,i4))
        Total_count += 1
    elif (i4,i2) in BlueEdges:
        RedEdges.append((i1,i3))
        BlueEdges.remove((i4,i2))
        Total_count += 1
    
    
    if (Total_count==2):
        RedEdges.remove((i1,i3))
        RedEdges.remove((i2,i4))
    
    if(Total_count>0):
         return i1,i2,i3,i4,Total_count
        
    count = 0
    if (i1,i4) in BlueEdges:
        RedEdges.append((i2,i3))
        BlueEdges.remove((i1,i4)) 
        i = i4
        i4 = i3
        i3 = i
        count += 1
        Total_count += 1
    elif (i4,i1) in BlueEdges:
        RedEdges.append((i2,i3))
        BlueEdges.remove((i4,i1))
        i = i4
        i4 = i3
        i3 = i
        count += 1
        Total_count += 1
    if(i2,i3) in BlueEdges:
        RedEdges.append((i1,i4))
        BlueEdges.remove((i2,i3))
        i = i4
        i4 = i3
        i3 = i
        count += 1
        Total_count += 1
    elif(i3,i2) in BlueEdges:
        RedEdges.append((i1,i4))
        BlueEdges.remove((i3,i2))
        i = i4
        i4 = i3
        i3 = i
        count += 1
        Total_count += 1
        
    if (count==2):
        RedEdges.remove((i1,i4))
        RedEdges.remove((i2,i3))
    
    if (Total_count == 0):
        RedEdges.append((i1,i2))
        RedEdges.append((i3,i4))
    
    return i1,i2,i3,i4,Total_count


# In[342]:


def ShortestRearrangementScenario(P, Q):
    output(P)
    RedEdges = ColoredEdges(P)
    BlueEdges = ColoredEdges(Q)
    BreakpointGraph  = RedEdges +  BlueEdges
    #while BreakpointGraph has a non-trivial cycle Cycle:
    #for i in range(3):
    n = len(BreakpointGraph)
    while n>=4:
        #(i1 , i2 , i3 , i4 ) ← path starting at arbitrary red edge in nontrivial red-blue cycle
        count = 0
        while count == 0:
            (i1,i2),(i3,i4) = random.sample(RedEdges,2)
        #BlueEdges,RedEdges,i1,i2,i3,i4  = FindTrivalCycle(BlueEdges,RedEdges,i1,i2,i3,i4)
            i1,i2,i3,i4,count = FindTrivalCycle(BlueEdges,RedEdges,i1,i2,i3,i4)
        #RedEdges = TwoBreakOnGenomeGraph(RedEdges, i1 , i2 , i3 , i4)
        #RedEdges ← RedEdges with edges (i1, i2) and (i3, i4) removed
        #RedEdges ← RedEdges with edges (i1, i4) and (i2, i3) added
        BreakpointGraph = RedEdges +  BlueEdges
        n = len(BreakpointGraph)
        
        P = TwoBreakOnGenome(P, i1 , i2 , i3 , i4 )
        output(P)

Sample Input:

(+1 -2 -3 +4)
(+1 +2 -4 -3)

Sample Output:

(+1 -2 -3 +4)
(+1 -2 -3)(+4)
(+1 -2 -4 -3)
(-3 +1 +2 -4)
# In[339]:


inp1='(+1 -2 -3 +4)'
inp2='(+1 +2 -4 -3)'


# In[346]:


P= PreProcess(inp1)
Q= PreProcess(inp2)


# In[333]:


P1 = TwoBreakOnGenome(P, 3, 6 , 8 , 1 )
P1


# In[334]:


P2 = TwoBreakOnGenome(P1, 5, 7 , 3 , 8)
P2


# In[347]:


ShortestRearrangementScenario(P, Q)


# In[ ]:


inp1 = '(+1 -2 -3 +4)'
i1,i2,i3,i4 = 2, 4, 8, 1


# In[352]:


file = open('dataset_369337_5.txt', 'r') 
inp1
inp2
for i, line in enumerate(file):
    line=line.rstrip('\n')
    if(i==0):
        inp1 = line
    else:
        inp2 = line


# In[353]:


P= PreProcess(inp1)
Q= PreProcess(inp2)


# In[354]:


ShortestRearrangementScenario(P, Q)


# In[ ]:




