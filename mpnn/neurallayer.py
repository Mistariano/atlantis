__author__ = 'MisT'

import NeuralNode


class NeuralLayer:
    def __init__(self,N=0,I=0):
        self.num=N
        self.inputs=I
        self.setit()
        self.nns=[]

    def setit(self):
        for i in range(0,self.num):
            self.nns.append(NeuralNode(self.inputs))

    def workout(self,input):
        if len(input)!=self.inputs:
            print 'opp2.'
            return [-1]
        ans=[]
        for i in range(0,self.num):
            res=self.nns[i].workout(input=input)
            if(res==-1):
                return [-1]
            ans.append(res)
        return ans

    def test(self):
        for i in self.nns:
            i.test()
