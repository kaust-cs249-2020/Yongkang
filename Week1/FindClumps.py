#!/usr/bin/env python
# coding: utf-8



def FrequencyTable(Text, k):
    freqMap = {}
    n  = len(Text)
    for i in range(n-k+1):
        Pattern  = Text[i:i+k]
        if Pattern not in freqMap.keys():
            freqMap[Pattern] = 1
        else:
            freqMap[Pattern]  = freqMap[Pattern]+1 
    return freqMap


# In[2]:


def FindClumps(Text, k, L, t):
    Patterns =  set()
    n  = len(Text)
    for i in range(n-L+1):
        Window = Text[i:i+L]
        freqMap = FrequencyTable(Window, k)
        for s in freqMap:
            if freqMap[s] >= t:
                Patterns.add(s)
    return Patterns


# In[3]:


Genome =  'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
k = 5
L = 50
t = 4


# In[4]:


FindClumps(Genome,k,L,t)


# In[5]:


Genome='' 
k=0
L=0
t=0
file = open('dataset_369235_5.txt', 'r') 
for i, line in enumerate(file):
    line=line.rstrip('\n')
    if(i==0):
        Genome = line
    else:
        (k ,L, t) = line.split(' ')
        k = int(k)
        L = int(L)
        t = int(t)
        


# In[6]:


Pattern = FindClumps(Genome,k,L,t)
for kmer in Pattern:
    print(kmer)


# In[7]:


Genome='' 
file = open('E_coli.txt', 'r') 
for i, line in enumerate(file):
    line=line.rstrip('\n')
    Genome = line




Pattern = FindClumps(Genome,9,500,3)


num = len(Pattern)
print(num)

OUT=open('Ecoli_num','w') 
OUT.write(num)







