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
    for i in range (0,SIZE_SENSOR+SIZE_OUTPUT+1):
        str.appendNeuron()
        g.thresholds.append(random.uniform(-0.5,0.5))
    for i in range(0,SIZE_SENSOR):
        str.appendSynapse(origin=i,terminus=SIZE_SENSOR+SIZE_OUTPUT)
        g.weights.append(random.uniform(-2,2))
        str.appendSynapse(origin=SIZE_SENSOR+SIZE_OUTPUT,terminus=i+SIZE_SENSOR)
        g.weights.append(random.uniform(-2,2))
    save.saveStruct(str.pack())
    g.set()
    sp1=Specie(members=[g],appearTime=0)
    nature=Nature(species=[sp1],generation=0,restResource=0)
    save.saveCurrent(nature.packCurrent())
    print'Initializing has been done.'
    # os.system('pause')

