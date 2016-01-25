__author__ = 'MisT'


class Node:
    def __init__(self,threshold):
        self.threshold=threshold
        self.battery=0
        self.sons=[]
        self.weights=[]

    def appendSon(self,son,weight):
        self.sons.append(son)
        self.weights.append(weight)

    def charge(self,quantity):
        self.battery+=(quantity-self.threshold)
        # print 'I\'m charged! Now my battery is',self.battery

    def discharge(self):
        q=self.sigmoid(self.battery)
        p=0
        for s in self.sons:
            s.charge(quantity=q*self.weights[p])
            p+=1
        self.battery=0
        # print 'PIKAPIKA~CHU!!!! (',q,')'
        return q

    def sigmoid(self,n):
        return 1/(1+pow(2.718,-n))

    def debug(self):
        print 'Infos of \'this\' node:'
        print 'Sons:',self.sons
        print 'Weights:',self.weights
        print 'Threshold:',self.threshold


if __name__=='__main__':
    n1=Node(threshold=0,numUnit=0)
    n2=Node(threshold=0,numUnit=1)
    # n1.sons.append(n2)
    n1.appendSon(son=n2,weight=2)
    n1.charge(1)
    print n2.battery
    print n1.discharge()
    print n2.battery





