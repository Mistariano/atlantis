__author__ = 'MisT'

from unit.unit import Unit
from random import choice
from gene.mate import mate
from gene.gene import Gene
from settings import SPEED_MUTATION,SPEED_MATE,SIZE_BOARD,SIZE_OUTPUT,SIZE_SENSOR
from unitplay import UnitPlay
from goplay.gopoint import GoPoint
import os

class Specie:
    def __init__(self,firstMember):
        self.genes=[firstMember]
        self.billyKing=0
        self.size=1
        self.newBorn=[]

    def load(self,gene):
        return Unit(gene=gene)

    def loop(self):
        r=[i for i in range(0,len(self.genes))]
        r.remove(self.billyKing)
        for i in range(0,SPEED_MATE):
            if not len(r):
                break
            wife=choice(r)
            new1=mate(gene1=self.genes[self.billyKing],gene2=self.genes[wife])
            self.newBorn.append(new1)
            r.remove(wife)
        for i in range(0,SPEED_MUTATION):
            tmp=choice(self.genes)
            new1=Gene(structure=tmp.structure,weights=tmp.weights,thresholds=tmp.thresholds)
            new1.mutation()
            self.newBorn.append(new1)
        self.sort()
        t=choice(self.genes)
        new2=Gene(structure=t.structure,weights=t.weights,thresholds=t.thresholds)
        new3=Gene(structure=t.structure,weights=t.weights,thresholds=t.thresholds)
        new2.addNRand()
        yield new2
        for n in new3.getSRand(sizeO=SIZE_OUTPUT,sizeS=SIZE_SENSOR):
            yield n


    def sort(self):
        for new in self.newBorn:
            un=self.load(gene=new)
            uk=self.load(gene=self.genes[self.billyKing])
            res=self.fight(newUnit=un, kingUnit=uk)
            if res>0:
                self.billyKing=self.size
            self.genes.append(new)
        self.newBorn=[]

    def fight(self,newUnit,kingUnit):
        newPlay1=UnitPlay(size=SIZE_BOARD)
        newPlay1.loadUnit(ub=newUnit,uw=kingUnit)
        newPlay1.loop()
        res=newPlay1.res_cnt[GoPoint.BLACK]-newPlay1.res_cnt[GoPoint.WHITE]
        newPlay2=UnitPlay(size=SIZE_BOARD)
        newPlay2.loadUnit(ub=kingUnit,uw=newUnit)
        newPlay2.loop()
        res+=newPlay2.res_cnt[GoPoint.WHITE]-newPlay2.res_cnt[GoPoint.BLACK]
        return res




