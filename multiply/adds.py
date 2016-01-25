__author__ = 'MisT'

from settings import RATE_ADDS,SIZE_SENSOR,SIZE_OUTPUT
from gene.gene import Gene
from random import choice


def addS(gene):
    g=Gene(listN=gene.listN,listS=gene.listS)
    l1=[i for i in range(0,SIZE_SENSOR) or i in range(SIZE_SENSOR+SIZE_OUTPUT,len(g.listN))]
    l2=[]
    t1=choice(l1)
    while not len(l2):
        lt=[]
        for s in g.listS and s.enable:
            if s.origin==t1:
                lt.append(s.terminus)
            if s.terminus==t1:
                lt.append(s.origin)
        l2=[i for i in range(SIZE_SENSOR,len(g.listN)) and i not in lt]
        if not len(l2):
            l1.remove(t1)
            if not len(l1):
                return false
            t1=choice(l1)
            continue
    t2=choice(l2)







