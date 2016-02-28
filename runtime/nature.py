__author__ = 'MisT'

from unit.unit import Unit
from unitplay import UnitPlay
from goplay.gopoint import GoPoint
from specie import Specie
from settings import MAX_SCORE,RESOURCE,SIZE_BOARD
from gene.gene import Gene,GeneStructure
from save import saveCurrent
import os


class Nature:
    def __init__(self,species,generation,restResource,):
        self.species=species
        self.generation=generation
        self.resource=restResource
        self.cntGenes=0
        self.menu={}

    def showInfo(self):
        print 'Generation:',self.generation
        print 'And now we have _%d_ genes'%self.cntGenes
        print 'In _%d_ species'%len(self.species)
        print 'Menu:'
        print self.menu

    def loop(self):
        self.cntGenes=0
        self.menu={}
        for s in self.species:
            self.cntGenes+=len(s.genes)
            self.menu[s.num]=[]
            for g in s.genes:
                self.menu[s.num].append(g.num)
        self.showInfo()
        averfitness=0.0
        newspecies=[]
        newgenes = []
        for s in self.species:
            s.breed()
            for n in s.newSpecies():
                newspecies.append(n)
        for n in newspecies:
            self.species.append(Specie(members=[n],appearTime=self.generation))
        for s in self.species:
            for n in s.newGenes():
                newgenes.append(n)
        while len(newgenes):
            n=newgenes[0]
            for s in self.species:
                for o in s.genes:
                    if o not in newgenes:
                        self.adjustFitness(new=n,old=o)
            del newgenes[0]
        for s in self.species:
            s.sort()
            s.recountFitness()
            averfitness+=s.fitness
        averfitness/=len(self.species)
        self.resource+=RESOURCE
        dieList=[]
        i=0
        while i <len(self.species):
            s=self.species[i]
            r=self.resource*(averfitness/(s.fitness+1))/len(self.species)
            print '[%d] get resource:%d'%(s.num,r)
            for d in s.distribute(resource=r):
                dieList.append(d)
            if not len(s.genes):
                print 'The specie [%d] has died out.'%s.num
                del self.species[i]
                continue
            i+=1
        self.resource=0.0
        while len(dieList):
            self.resource+=self.happyCorner(unlucky=dieList[0])
            del dieList[0]
        saveCurrent(self.packCurrent())
        self.generation+=1

    def fight(self,newUnit,oldUnit):
        newPlay1=UnitPlay(size=SIZE_BOARD)
        newPlay1.loadUnit(ub=newUnit,uw=oldUnit)
        newPlay1.loop()
        res=newPlay1.res_cnt[GoPoint.BLACK]-newPlay1.res_cnt[GoPoint.WHITE]
        newPlay2=UnitPlay(size=SIZE_BOARD)
        newPlay2.loadUnit(ub=oldUnit,uw=newUnit)
        newPlay2.loop()
        res+=newPlay2.res_cnt[GoPoint.WHITE]-newPlay2.res_cnt[GoPoint.BLACK]
        return res

    def load(self,gene):
        return Unit(gene=gene)

    def adjustFitness(self,new,old):
        print 'There\'s a fight between Gene <%d> and <%d>' % (new.num,old.num)
        uo=self.load(gene=old)
        un=self.load(gene=new)
        res=self.fight(newUnit=un,oldUnit=uo)
        new.fitness+=(MAX_SCORE-res)/2
        old.fitness+=(MAX_SCORE+res)/2
        new.record[old.num]=(MAX_SCORE-res)/2
        old.record[new.num]=(MAX_SCORE+res)/2

    def happyCorner(self,unlucky):
        print 'Gene <%d> has gone die QAQ' % unlucky.num
        print 'It\'s fitness is',unlucky.fitness
        for s in self.species:
            for i in s.genes:
                if i !=unlucky:
                    i.fitness-=i.record[unlucky.num]
        return unlucky.fitness

    def packCurrent(self):
        current=\
        {
            '_id':0,
            'gene':Gene.cnt,
            'structure':GeneStructure.cnt,
            'generation':self.generation,
            'restRes':self.resource
        }
        info=[current]
        i=1
        for s in self.species:
            current=\
            {
                '_id':i,
                'num':s.num,
                'genes':[gene.num for gene in s.genes],
                'appear':s.appearTime
            }
            i+=1
            info.append(current)
        return info



