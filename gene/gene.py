__author__ = 'MisT'

from genestructure import GeneStructure
from random import randrange,choice
from copy import deepcopy


class Gene:
    cnt=0
    def __init__(self,structure,weights,thresholds):
        self.numNature=Gene.cnt
        Gene.cnt+=1
        self.structure=structure
        self.numSpecie=self.structure.nextMember
        self.structure.member+=1
        self.structure.nextMember+=1
        self.weights=deepcopy(weights)
        self.thresholds=deepcopy(thresholds)
        self.fitness=0
        # print 'Gene no.%d has been created!'%self.numNature
        # print 'and it\'s the',self.numSpecie,'member of Specie no.',self.structure.num

    def addNRand(self):
        new=GeneStructure(gsNew=self.structure)
        r=randrange(0,new.sizeS)
        new.appendNeuron()
        self.thresholds.append(0)
        p=0
        pi=0
        tar=new.appendNeuron()
        for i in range(0,new.sizeN):
            pi=p
            for j in new.neurons[i]:
                if p==r:
                    p=-1
                    new.neurons[i].remove(j)
                    new.sizeS-=1
                    new.appendSynapse(origin=tar,terminus=j)
                    self.weights.append(self.weights[r])
                    del self.weights[r]
                    break
            if p<0:
                new.appendSynapse(origin=i,terminus=tar)
                p=pi+len(new.neurons[i])-1
                self.weights.insert(p,1)
                break
            p+=1
        self.structure=new
        self.structure.sort()
        print 'Gene no.%d get a new neuron'%self.numNature

    def check(self,x,f):
        if x==f:
            return 0
        if not len(self.structure.neurons[x]):
            return 1
        for i in self.structure.neurons[x]:
            if not dfs(i,f):
                return 0
        return 1

    def getSRand(self,sizeS,sizeO):
        neu=self.structure.neurons
        t1=-1
        r1=[i for i in range(0,sizeS) or i in range(sizeS+sizeO,self.structure.sizeN)]
        r2=[]
        while not len(r2):
            try:
                r1.remove(t1)
            except:
                pass
            t1=choice(r1)
            r2=[i for i in range(sizeS,self.structure.sizeN)and i not in neu[t1]]
        t2=choice(r2)
        passCheck=1
        if self.check(t1,t2):
            passCheck=0
            new1=GeneStructure(gsNew=self.structure)
            new1.appendSynapse(origin=t1,terminus=t2)
            p=0
            flag=0
            for i in range(0,new1.sizeN):
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
            yield Gene(structure=new1,weights=wn1,thresholds=tn1)
        if passCheck or self.check(t2,t1):
            new2=GeneStructure(gsNew=self.structure)
            new2.appendSynapse(origin=t2,terminus=t1)
            p=0
            flag=0
            for i in range(0,new2.sizeN):
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
            yield Gene(structure=new2,weights=wn2,thresholds=tn2)

    def debug(self):
        print 'Infos of \'this\' gene:'
        print 'Nature number:',self.numNature
        print 'Member number:',self.numSpecie
        print 'Fitness(current):',self.fitness
        print 'Weights:',self.weights
        print 'Thresholds:',self.thresholds
        print 'About its Structure:'
        self.structure.debug()