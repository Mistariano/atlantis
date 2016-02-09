__author__ = 'MisT'

from gene import Gene
from random import randrange

def mate(gene1,gene2):
    # print'in mate'
    w1=gene1.weights
    w2=gene2.weights
    # print'w1:',len(w1),w1
    # print'w2:',len(w2),w2
    w3=[]
    for i in range(0,len(w1)):
        if randrange(0,2):
            w3.append(w1[i])
        else:
            w3.append(w2[i])
    t1=gene1.thresholds
    t2=gene2.thresholds
    t3=[]
    for i in range(0,len(t1)):
        if randrange(0,2):
            t3.append(t1[i])
        else:
            t3.append(t2[i])
    g=Gene(structure=gene1.structure,weights=w3,thresholds=t3)
    g.set()
    return g