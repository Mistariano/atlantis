__author__ = 'MisT'

from gene.gene import Gene
from settings import RATE_MUTATION,MAX_N,MAX_S
from random import uniform


def mutation(gene):
    g=Gene(listS=gene.listS,listN=gene.listN,order=gene.order)
    flag=False
    for n in g.listN:
        if uniform(0,1)<RATE_MUTATION:
            flag=True
            n.threshold+=uniform(0-MAX_N,MAX_N)
    for s in g.listS:
        if uniform(0,1)<RATE_MUTATION:
            flag=True
            s.threshold+=uniform(0-MAX_S,MAX_S)
    if flag:
        return g
    else:
        return False
