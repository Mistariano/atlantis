__author__ = 'MisT'

from node import Node
from settings import SIZE_OUTPUT,SIZE_SENSOR


class Unit:
    def __init__(self,gene):
        self.gene=gene
        self.size=0
        self.neurons=[]
        self.fathers=[]
        self.order=gene.order
        self.layerSensor=[i for i in range(0,SIZE_SENSOR)]
        self.layerOutput=[i for i in range(SIZE_SENSOR,SIZE_SENSOR+SIZE_OUTPUT)]
        self.index={}
        self.translate()
        self.sort()

    def translate(self):
        p=0
        for n in self.gene.listN:
            self.neurons.append(Node(threshold=n.threshold,numUnit=p))
            self.index[n.num]=p
            self.size+=1
            p+=1
        self.fathers=[0 for i in range(0,self.size)]
        for s in self.gene.listS:
            indexFather=self.index[s.origin]
            indexSon=self.index[s.terminus]
            self.neurons[indexFather].appendSon(son=self.neurons[indexSon],weight=s.weight)
            self.fathers[indexSon]+=1

    def sort(self):
        if not len(self.order):
            i=0
            cnt=0
            while(cnt<self.size):
                if not self.fathers[i]:
                    if len(self.neurons[i].sons):
                        for n in self.neurons[i].sons:
                            self.fathers[n.numUnit]-=1
                        self.order.append(i)
                        self.fathers[i]=-1
                    cnt+=1
                i=(i+1)%self.size

    def startDash(self,inputs):
        p=0
        for i in self.layerSensor:
            self.neurons[i].charge(quantity=inputs[p])
            p+=1
        for i in self.order:
            self.neurons[i].discharge()
        outputs=[self.neurons[o].discharge() for o in self.layerOutput]
        # print outputs
        return outputs

if __name__=='__main__':
    from gene.gene import Gene
    from gene.geneneuron import GeneNeuron
    from gene.genesynapse import GeneSynapse
    import random

    gn=[GeneNeuron(num=i,threshold=random.uniform(0,1)) for i in range(0,6)]
    gs=[]
    gs.append(GeneSynapse(origin=0,terminus=4,weight=random.uniform(0,1)))
    gs.append(GeneSynapse(origin=0,terminus=5,weight=random.uniform(0,1)))
    gs.append(GeneSynapse(origin=1,terminus=5,weight=random.uniform(0,1)))
    gs.append(GeneSynapse(origin=4,terminus=3,weight=random.uniform(0,1)))
    gs.append(GeneSynapse(origin=4,terminus=2,weight=random.uniform(0,1)))
    gs.append(GeneSynapse(origin=5,terminus=2,weight=random.uniform(0,1)))
    g=Gene(listN=gn,listS=gs)
    u=Unit(gene=g)
    u.startDash(inputs=[1,0])






