__author__ = 'MisT'

from runtime.nature import Nature
from settings import MAX_GENERATION_PER
from gene.gene import Gene
from gene.genestructure import GeneStructure
from runtime.specie import Specie
import random
import os
str=GeneStructure(gsNew=-1)
g=Gene(structure=str,weights=[],thresholds=[])
for i in range (0,147):
    str.appendNeuron()
    g.thresholds.append(random.uniform(-0.5,0.5))
for i in range(0,49):
    for j in range(0,49):
        str.appendSynapse(origin=i,terminus=j+98)
        str.appendSynapse(origin=i+98,terminus=j+49)
        g.weights.append(random.uniform(-2,2))
        g.weights.append(random.uniform(-2,2))
str.sort()
sp1=Specie(firstMember=g,appearTime=0)
nature=Nature(firstSpecie=sp1)
for i in range(0,MAX_GENERATION_PER):
    nature.loop()
