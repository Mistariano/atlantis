__author__ = 'MisT'

from copy import deepcopy
from unit.unit import Unit
from random import choice
from gene.mate import mate
from gene.gene import Gene
from settings import SPEED_MUTATION,SPEED_MATE,SIZE_BOARD,SIZE_OUTPUT,SIZE_SENSOR,WHO_MATE

class Specie:
    def __init__(self,members,appearTime):
        self.genes=members
        self.newBorn=[]
        self.newSpiecesList=[]
        self.dieList=[]
        self.newGenesList=members
        self.billyKing=members[0]
        self.appearTime=appearTime
        self.fitness=0
        self.sum=0
        self.num=members[0].structure.num
        print 'Specie [%d] has been settled.' % self.num

    def load(self,gene):
        return Unit(gene=gene)

    def breed(self):
        if len(self.genes)>1:
            r=[i for i in (1,WHO_MATE) if i<len(self.genes)]
            for i in range(0,SPEED_MATE):
                wife=choice(r)
                new1=mate(gene1=self.genes[0],gene2=self.genes[wife])
                self.newGenesList.append(new1)
                self.genes.append(new1)
        for i in range(0,SPEED_MUTATION):
            tmp=choice(self.genes)
            new1=Gene(structure=tmp.structure,weights=tmp.weights,thresholds=tmp.thresholds)
            new1.mutation()
            self.newGenesList.append(new1)
            self.genes.append(new1)
        t=choice(self.genes)
        new2=Gene(structure=t.structure,weights=t.weights,thresholds=t.thresholds)
        new3=Gene(structure=t.structure,weights=t.weights,thresholds=t.thresholds)
        new2.addNRand()
        self.newSpiecesList.append(new2)
        for n in new3.getSRand(sizeO=SIZE_OUTPUT,sizeS=SIZE_SENSOR):
            self.newSpiecesList.append(n)

    def newSpecies(self):
        for n in self.newSpiecesList:
            yield n
        self.newSpiecesList=[]

    def newGenes(self):
        for n in self.newGenesList:
            yield n
        self.newGenesList=[]

    def sort(self):
        self.genes.sort(key=lambda x:x.fitness)
        self.billyKing=self.genes[0]

    def recountFitness(self):
        self.sum=0
        for g in self.genes:
            self.sum+=g.fitness
        # self.fitness=len(self.genes)*self.sum
        self.fitness=self.sum

    def distribute(self,resource):
        while len(self.genes):
            if (self.sum-self.genes[-1].fitness)<=resource:
                break
            self.sum-=self.genes[-1].fitness
            yield self.genes[-1]
            del self.genes[-1]

if __name__=='__main__':
    class Test:
        cnt=0
        def __init__(self):
            self.num=Test.cnt
            Test.cnt+=1
            self.weights=[self.num]
            self.f=10-self.num
    t=[Test() for i in range(0,7)]
    t2=[Test()]
    t.append(t2[0])
    del t[-1]
    print t2




