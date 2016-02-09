__author__ = 'MisT'

from runtime.nature import Nature
from settings import MAX_GENERATION_PER,SIZE_SENSOR,SIZE_OUTPUT,INIT
from gene.gene import Gene
from gene.genestructure import GeneStructure
from runtime.specie import Specie
from pymongo import MongoClient
from gene.genestructure import GeneStructure
from copy import deepcopy
from runtime.specie import Specie
from runtime.initialize import init
from runtime import save
import random
import os

if INIT:
    init()
connect=MongoClient().atlantis
current=connect['current'].find()[0]
cntGene=current['gene']
cntStructure=current['structure']
Gene.cnt=cntGene
GeneStructure.cnt=cntStructure
generation=current['generation']
restRes=current['restRes']
spicies=connect['current'].find()
geneBase=connect['gene']
structBase=connect['structure']

spicieList=[]
for s in spicies:
    if not s['_id']:
        continue
    num=s['num']
    genes=s['genes']
    appear=s['appear']
    structInfo=structBase.find({'_id':num})[0]
    neurons=structInfo['neurons']
    size=structInfo['size']
    structure=GeneStructure(gsNew=-1,fromDB=1,num=num,neurons=neurons,sizeS=size)
    members=[]
    for g in genes:
        curGene=geneBase.find({'_id':g})[0]
        weights=curGene['weights']
        thresholds=curGene['thresholds']
        fitness=curGene['fitness']
        record=curGene['record']
        num=curGene['_id']
        gene=Gene(structure=structure,weights=weights,thresholds=thresholds,fitness=fitness,record=record,num=num)
        members.append(gene)
    spicie=Specie(members=members,appearTime=appear)
    spicieList.append(spicie)

nature=Nature(species=spicieList,generation=generation,restResource=restRes)

for i in range(0,MAX_GENERATION_PER):
    nature.loop()

save.saveCurrent(nature.packCurrent())

# structures={}
# genes={}
# species=[]
#
# # connect=MongoClient().atlantis
# # dbGene=connect['gene']
# # dbStructure=connect['structure']
# # dbGeneration=connect['generation']
# # dbCurrent=connect['current']
# # dbCurStru=connect['curstru']
# # dbCurGn=connect['curgn']
# # dbCurSp=connect['cursp']
# #
# # for s in dbCurStru.find():
# #     num=s['_id']
# #     neurons=deepcopy(s['neurons'])
# #     strc=GeneStructure(gsNew=-1)
# #     strc.num=num
# #     strc.neurons=neurons
# #     strc.sort()
# #     structures[num]=strc
# # for g in dbCurGn.find():
# #     num=g['_id']
# #     strc=g['structure']
# #     weights=g['weights']
# #     thresholds=g['thresholds']
# #     fitness=g['fitness']
# #     gn=Gene(structure=structures[strc],weights=weights,thresholds=thresholds)
# #     gn.num=num
# #     gn.fitness=fitness
# #     genes[num]=gn
# # for s in dbCurSp.find():
# #     num=s['_id']
# #     appearTime=s['appear']
# #     gns=s['genes']
# #     members=[genes[g] for g in gns]
# #     sp=Specie(members=members,appearTime=appearTime)
# #     sp.num=num
# #     species.append(sp)
# str=GeneStructure(gsNew=-1)
# g=Gene(structure=str,weights=[],thresholds=[])
# g.set()
# for i in range (0,SIZE_SENSOR+SIZE_OUTPUT):
#     str.appendNeuron()
#     g.thresholds.append(random.uniform(-0.5,0.5))
# for i in range(0,SIZE_SENSOR):
#     for j in range(SIZE_SENSOR,SIZE_SENSOR+SIZE_OUTPUT):
#         str.appendSynapse(origin=i,terminus=j)
#         g.weights.append(random.uniform(-2,2))
#         g.weights.append(random.uniform(-2,2))
# str.sort()
# sp1=Specie(members=[g],appearTime=0)
# nature=Nature(species=[sp1])
# # nature=Nature(species=species)
# for i in range(0,MAX_GENERATION_PER):
#     nature.loop()
