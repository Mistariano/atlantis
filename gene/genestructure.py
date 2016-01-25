__author__ = 'MisT'

import copy


class GeneStructure:
    cnt=0

    def __init__(self,gsNew=-1):
        self.num=cnt
        GeneStructure.cnt+=1
        self.order=[]
        try:
            self.neurons=copy.deepcopy(gsNew.neurons)
            self.sizeN=gsNew.sizeN
            self.sizeS=gsNew.sizeS
            self.member=gsNew.member
        except:
            self.neurons={}
            self.sizeN=0
            self.sizeS=0
            self.member=0


    def addNeuron(self):
        self.neurons[self.sizeN]=[]
        self.sizeN+=1

    def addSynapse(self,origin,terminus):
        self.neurons[origin].append(terminus)
        self.sizeS+=1

    def sort(self):
        father=[0]*self.size
        p=0
        for i in self.neurons:
            for j in i:
                father[j]+=1
        for i in range(0,self.size):
            if not father[i]:
                self.order.append(i)
        while p<len(self.order):
            for j in self.neurons[self.order[p]]:
                father[j]-=1
                if not father[j]:
                    self.order.append(j)
            p+=1

if __name__=='__main__':
    g=GeneStructure()






