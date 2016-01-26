__author__ = 'MisT'

from node import Node
from settings import SIZE_OUTPUT,SIZE_SENSOR


class Unit:
    def __init__(self,gene):
        self.gene=gene
        self.structure=gene.structure
        self.neurons=[]
        self.order=gene.structure.order
        self.layerSensor=[i for i in range(0,SIZE_SENSOR)]
        self.layerOutput=[i for i in range(SIZE_SENSOR,SIZE_SENSOR+SIZE_OUTPUT)]
        self.index={}
        self.translate()

    def translate(self):
        p=0
        self.neurons=[Node(threshold=i) for i in self.gene.thresholds]
        for i in range(0,len(self.structure.neurons)):
            for j in self.structure.neurons[i]:
                self.neurons[i].appendSon(son=self.neurons[j],weight=self.gene.weights[p])
                p+=1

    def startDash(self,inputs):
        p=0
        for i in self.layerSensor:
            self.neurons[i].charge(quantity=inputs[p])
            p+=1
        # print 'size:',len(self.neurons)
        for i in self.order :
            if i not in self.layerOutput:
                # print'i:',i
                self.neurons[i].discharge()
        outputs=[self.neurons[o].discharge() for o in self.layerOutput]
        # print outputs
        return outputs

    def debug(self):
        print 'Infos of \'this\' unit:'
        print 'Neurons:'
        for i in range(0,len(self.neurons)):
            print 'No.',i,':'
            self.neurons[i].debug()
        print 'Gene:'
        self.gene.debug()

if __name__=='__main__':
    from gene.gene import Gene
    from gene.genestructure import GeneStructure
    import random
    str=GeneStructure(gsNew=-1)
    g=Gene(structure=str,weights=[],thresholds=[])
    for i in range (0,60):
        str.appendNeuron()
        g.thresholds.append(random.uniform(-0.5,0.5))
    for i in range(0,20):
        for j in range(20,40):
            str.appendSynapse(origin=i,terminus=j)
            str.appendSynapse(origin=j,terminus=i+40)
            g.weights.append(random.uniform(-2,2))
            g.weights.append(random.uniform(-2,2))
    # str.appendSynapse(origin=0,terminus=4)
    # str.appendSynapse(origin=0,terminus=5)
    # str.appendSynapse(origin=1,terminus=5)
    # str.appendSynapse(origin=4,terminus=3)
    # str.appendSynapse(origin=4,terminus=2)
    # str.appendSynapse(origin=5,terminus=2)
    str.sort()
    # for i in range(0,6):
    #     g.weights.append(random.uniform(0,2))
    u=Unit(gene=g)
    # u.debug()
    for i in range(0,10):
        print i
        u.startDash(inputs=[1,0]*10)






