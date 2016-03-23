#coding:utf8
__author__ = 'MisT'

from unit import Unit

class UnitGroup:
    def __init__(self,genes):
        self.units=[Unit(gene=g) for g in genes]

    def output(self,inputs):
        if not len(units):
            return[]
        output=units[0].startDash(inputs=inputs)
        for i in xrange(1,len(units)):
            temp=units[i].startDash(inputs=inputs)
            for j in xrange(0,len(temp)):
                output[j]+=temp[j]
        return output

