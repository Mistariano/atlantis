__author__ = 'MisT'


class GeneNeuron:
    # HIDDEN=0
    # SENSOR=1
    # OUTPUT=-1
    def __init__(self,num,threshold):
        self.num=num
        self.threshold=threshold
        # self.state=state       #0:HIDDEN,1:SENSOR,-1:OUTPUT

if __name__=='__main__':
    l=[GeneNeuron(num=0,threshold=1),GeneNeuron(num=1,threshold=1)]
    for i in l:
        i.num+=1
    for i in l:
        print i.num

