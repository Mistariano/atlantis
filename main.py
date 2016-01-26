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
for i in range (0,21):
    str.appendNeuron()
    g.thresholds.append(random.uniform(-0.5,0.5))
for i in range(0,7):
    for j in range(7,14):
        str.appendSynapse(origin=i,terminus=j+7)
        str.appendSynapse(origin=i+14,terminus=j)
        g.weights.append(random.uniform(-2,2))
        g.weights.append(random.uniform(-2,2))
str.sort()
sp1=Specie(firstMember=g)
nature=Nature(firstSpecie=sp1)
for i in range(0,MAX_GENERATION_PER):
    nature.loop()
