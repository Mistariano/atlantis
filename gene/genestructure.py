__author__ = 'MisT'

import copy
import os


class GeneStructure:
    cnt=0
    def __init__(self,gsNew,fromDB=0,num=-1,neurons=[],sizeS=0):
        self.order=[]
        if not fromDB:
            try:
                GeneStructure.cnt+=1
                self.num=GeneStructure.cnt
                self.neurons=copy.deepcopy(gsNew.neurons)
                self.sizeS=gsNew.sizeS
            except Exception,e:
                print Exception,e
        else:
            self.num=num
            self.neurons=copy.deepcopy(neurons)
            self.sizeS=sizeS
            self.sort()

    def pack(self):
        return {'_id':self.num,'neurons':self.neurons,'size':self.sizeS}

    def appendNeuron(self):
        self.neurons.append([])
        return len(self.neurons)-1

    def appendSynapse(self,origin,terminus):
        self.neurons[origin].append(terminus)
        self.sizeS+=1

    def sort(self):
        father=[0 for i in range(0,len(self.neurons))]
        p=0
        for i in self.neurons:
            for j in i:
                father[j]+=1
        for i in range(0,len(self.neurons)):
            if not father[i]:
                father[i]=-1
                self.order.append(i)
        while p<len(self.neurons):
            for j in self.neurons[self.order[p]]:
                father[j]-=1
                if not father[j]:
                    father[j]=-1
                    self.order.append(j)
            p+=1

    def debug(self):
        print 'Infos of \'this\' structure:'
        print 'No.',self.num
        print 'Neurons:',self.neurons
        print 'Order:',self.order
        print 'Size of neurons:',self.sizeN
        print 'Size of Synapses:',self.sizeS

if __name__=='__main__':
    g=GeneStructure(gsNew=-1)






