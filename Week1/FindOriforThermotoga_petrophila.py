#!/usr/bin/env python
# coding: utf-8

# In[2]:
print('hi')

def reverseSeq(sequence):
    reverse_dict = {'A':'T','T':'A','C':'G','G':'C'}
    sequence_rc = ''
    for base in sequence:
        sequence_rc = reverse_dict[base]+sequence_rc
    return sequence_rc


# In[3]:


def Hamming_distance(Seq1,Seq2):
    Distance = 0
    for i in range(len(Seq1)):
        if(Seq1[i] != Seq2[i]):
            Distance += 1
    return Distance


# In[4]:


def Neighbors(Pattern, d):
    nucleotides = {'A','C','G','T'}
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1: 
        return nucleotides
    Neighborhood = set()
    SuffixNeighbors = Neighbors(Pattern[1:len(Pattern)], d)
    for Text in SuffixNeighbors:
        if Hamming_distance(Pattern[1:len(Pattern)], Text) < d:
            for x in nucleotides:
                Neighborhood.add(x+Text)
        else:
            Neighborhood.add(Pattern[0]+Text)
    return Neighborhood


# In[5]:


def MaxMap(dic):
    max = -11111111111111111
    for key,value in dic.items():
        if(max<value):
            max = value
    return max


# In[12]:


def FrequentWordsWithMismatches(Text, k, d):
    Patterns = set()
    freqMap = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern =  Text[i:i+k]
        neighborhood = Neighbors(Pattern, d)
        for neighbor in neighborhood:
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] = freqMap[neighbor] + 1
    
        Pattern_rc = reverseSeq(Pattern)
        neighborhood_rc = Neighbors(Pattern_rc, d)
        for neighbor in neighborhood_rc:
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] = freqMap[neighbor] + 1
        
    m = MaxMap(freqMap)
    for Pattern in freqMap:
        if (freqMap[Pattern] == m) :
            Patterns.add(Pattern)
    return Patterns


# In[13]:


Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d=1


# In[14]:


FrequentWordsWithMismatches(Text, k, d)


# In[15]:


Pattern = ''
k = 0
d = 0
file = open('dataset_369239_10.txt', 'r') 
for i, line in enumerate(file):
    line=line.rstrip('\n')
    if(i==0):
        Pattern= line
    else:
        (k,d)= line.split(' ')
        k = int(k)
        d = int(d)
        




FrequentWordsWithMismatches(Pattern, k, d)




for pattern in FrequentWordsWithMismatches(Pattern, k, d):
    print(pattern,end=' ')




file = open('Salmonella_enterica.txt', 'r') 
sequence = ''
for i, line in enumerate(file):
	line=line.rstrip('\n')
	if(i!=0):
	   sequence = sequence + line



for pattern in FrequentWordsWithMismatches(sequence,9, 2):
    print(pattern,end=' ')



