__author__ = 'MisT'

import copy


class GeneStructure:
    cnt=0
    def __init__(self,gsNew):
        self.num=GeneStructure.cnt
        GeneStructure.cnt+=1
        self.order=[]
        self.member=0
        self.nextMember=0
        try:
            self.neurons=copy.deepcopy(gsNew.neurons)
            self.sizeN=gsNew.sizeN
            self.sizeS=gsNew.sizeS
        except:
            self.neurons=[]
            self.sizeN=0
            self.sizeS=0

    def appendNeuron(self):
        self.neurons.append([])
        self.sizeN+=1
        return self.sizeN-1

    def appendSynapse(self,origin,terminus):
        self.neurons[origin].append(terminus)
        self.sizeS+=1

    def sort(self):
        father=[0]*self.sizeN
        p=0
        for i in self.neurons:
            for j in i:
                father[j]+=1
        for i in range(0,self.sizeN):
            if not father[i]:
                self.order.append(i)
        while p<len(self.order):
            for j in self.neurons[self.order[p]]:
                father[j]-=1
                if not father[j]:
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






