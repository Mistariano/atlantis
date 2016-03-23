__author__ = 'MisT'

import NeuralLayer

class NeuralNet:
    def __init__(self,N,L,cnt=-1):
        self.num=N
        self.per_L=L
        self.cnt=cnt
        self.nls=[]
        self.setit()

    def setit(self):
        self.nls.append(NeuralLayer(N=self.per_L[0],I=self.per_L[0]))
        for i in range(1,self.num):
            self.nls.append(NeuralLayer(N=self.per_L[i],I=self.per_L[i-1]))

        if self.cnt==-1:
            self.cnt=self.per_L[0]*(self.per_L[0]+1)
            for i in range(1,self.num):
                self.cnt+=self.per_L[i]*(self.per_L[i-1]+1)

    def workout(self,input):
        for i in range(0,self.num):
            input=self.nls[i].workout(input=input)
            if input[0]==-1:
                print 'opp3.'
                return
        return input

    def test(self):
        print 'cnt=',self.cnt
        for i in range(0,self.num):
            self.nls[i].test()


