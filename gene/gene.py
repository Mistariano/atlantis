__author__ = 'MisT'

from genestructure import GeneStructure
from random import randrange,choice,uniform
from copy import deepcopy
from settings import RATE_MATE,MAX_S,MAX_N
from runtime import save
import sys


class Gene:
    cnt=0
    def __init__(self,structure,weights,thresholds,fitness=0,record={},num=-1):
        self.num=num
        self.structure=structure
        self.weights=deepcopy(weights)
        self.thresholds=deepcopy(thresholds)
        self.fitness=fitness
        self.record=record

    def pack(self):
        try:
            if self.num==-1:
                raise NumException
            info=\
            {
                '_id':self.num,
                'weights':self.weights,
                'thresholds':self.thresholds,
                'fitness':self.fitness,
                # 'record':self.record
                'record':{}
            }
            return info
        except NumException:
            print 'NumException'
        except Exception,e:
            print Exception,e


    def set(self):
        self.num=Gene.cnt
        Gene.cnt+=1
        save.saveGene(info=self.pack())
        print 'Gene <%d> has been born @w@' % self.num

    def addNRand(self):
        new=GeneStructure(gsNew=self.structure)
        r=randrange(0,len(self.weights))
        self.thresholds.append(0)
        tar=new.appendNeuron()
        p=0
        for i in range(0,len(new.neurons)):
            tmp=p
            for j in new.neurons[i]:
                if p==r:
                    new.neurons[i].remove(j)
                    p=-1
                    new.sizeS-=1
                    new.appendSynapse(origin=tar,terminus=j)
                    self.weights.append(self.weights[r])
                    del self.weights[r]
                    break
                p+=1
            if p<0:
                new.appendSynapse(origin=i,terminus=tar)
                p=tmp+len(new.neurons[i])
                self.weights.insert(p,1)
                break
        self.structure=new
        self.structure.sort()
        save.saveStruct(info=new.pack())
        self.set()

    def check(self,x,f,size,mark):
        if x*size+f in mark:
            return 1
        mark.append(x*size+f)
        if x==f:
            return 0
        if not len(self.structure.neurons[x]):
            return 1
        for i in self.structure.neurons[x]:
            if not self.check(x=i,f=f,size=size,mark=mark):
                return 0
        return 1

    def getSRand(self,sizeS,sizeO):
        neu=self.structure.neurons
        t1=-1
        r1=[i for i in range(0,sizeS) or i in range(sizeS+sizeO,self.structure.sizeN)]
        r2=[]
        while not len(r2):
            if t1!=-1:
                try:
                    r1.remove(t1)
                except Exception,e:
                    print Exception,e
                    print t1
            if not len(r1):
                return
            t1=choice(r1)
            r2=[i for i in range(sizeS,len(self.structure.neurons)) if (i not in neu[t1] and t1 not in neu[i])]
        t2=choice(r2)
        mark=[]
        size=len(neu)
        if self.check(x=t2,f=t1,size=size,mark=mark):
            passCheck=0
        else:
            passCheck=1
            new1=GeneStructure(gsNew=self.structure)
            new1.appendSynapse(origin=t1,terminus=t2)
            p=0
            flag=0
            for i in range(0,len(new1.neurons)):
                for j in new1.neurons[i]:
                    if j==t2:
                        flag=1
                        break
                    p+=1
                if flag:
                    break
            wn1=self.weights
            wn1.insert(p,0)
            tn1=self.thresholds
            new1.sort()
            save.saveStruct(info=new1.pack())
            g=Gene(structure=new1,weights=wn1,thresholds=tn1)
            g.set()
            yield g
        mark=[]
        if passCheck or self.check(x=t1,f=t2,size=size,mark=mark):
            new2=GeneStructure(gsNew=self.structure)
            new2.appendSynapse(origin=t2,terminus=t1)
            p=0
            flag=0
            for i in range(0,len(new2.neurons)):
                for j in new2.neurons[i]:
                    if j==t1:
                        flag=1
                        break
                    p+=1
                if flag:
                    break
            wn2=self.weights
            wn2.insert(p,0)
            tn2=self.thresholds
            new2.sort()
            save.saveStruct(info=new2.pack())
            g=Gene(structure=new2,weights=wn2,thresholds=tn2)
            g.set()
            yield g

    def mutation(self):
        for i in range(0,len(self.weights)):
            if uniform(0,1)<RATE_MATE:
                self.weights[i]+=uniform(0-MAX_S,MAX_S)
        for i in range(0,len(self.thresholds)):
            if uniform(0,1)<RATE_MATE:
                self.thresholds[i]+=uniform(0-MAX_N,MAX_N)
        self.set()

    def debug(self):
        print 'Infos of \'this\' gene:'
        print 'Nature number:',self.numNature
        print 'Member number:',self.numSpecie
        print 'Fitness(current):',self.fitness
        print 'Weights:',self.weights
        print 'Thresholds:',self.thresholds
        print 'About its Structure:'
        self.structure.debug()