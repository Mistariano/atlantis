__author__ = 'MisT'

import random

class NeuralNode:
    def __init__(self,N=0):
        self.setit(N)

    def setit(self,N):
        self.num=N
        self.weight=[]
        #self.threshold=random.uniform(0,1)
        for i in range(0,N+1):
            self.weight.append(random.uniform(0,1))

    def workout(self,input):
        if len(input)!=self.num:
            print 'opp1.'
            return -1
        ans=0
        for i in range(0,self.num):
            ans+=input[i]*self.weight[i]
        ans=sigmoid(ans)
        #ans-=self.threshold
        #ans-=self.weight[self.num]
        #print ans
        #if ans>=0:
            #return 1
            #return ans
        #return 0
        return max(ans,self.weight[self.num])

    def test(self):
        #for i in range(0,self.num+1):
        #    print self.weight[i]
        print self.weight

def sigmoid(n):
    return 1/(1+pow(2.718,n))