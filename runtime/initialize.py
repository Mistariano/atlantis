__author__ = 'MisT'


from settings import *
from gene.gene import GeneStructure,Gene
from specie import Specie
from nature import Nature
from save import drop
import random
import save
import os

def init():
    drop()
    print'Initializing...'
    str=GeneStructure(gsNew=-1,fromDB=1,num=0)
    g=Gene(structure=str,weights=[],thresholds=[],num=0)
    for i in range (0,SIZE_SENSOR+SIZE_OUTPUT):
        str.appendNeuron()
        g.thresholds.append(random.uniform(-0.5,0.5))
    for i in range(0,SIZE_SENSOR):
        for j in range(SIZE_SENSOR,SIZE_SENSOR+SIZE_OUTPUT):
            str.appendSynapse(origin=i,terminus=j)
            g.weights.append(random.uniform(-2,2))
            g.weights.append(random.uniform(-2,2))
    save.saveStruct(str.pack())
    g.set()
    sp1=Specie(members=[g],appearTime=0)
    nature=Nature(species=[sp1],generation=0,restResource=0)
    save.saveCurrent(nature.packCurrent())
    print'Done.'
    os.system('pause')

