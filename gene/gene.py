__author__ = 'MisT'
from geneneuron import GeneNeuron
from genesynapse import GeneSynapse
import copy


class Gene:
    def __init__(self,listN,listS,order=[]):
        self.listN=copy.deepcopy(listN)
        self.listS=copy.deepcopy(listS)
        self.order=order

    def appendN(self,neuron):
        self.listN.append(neuron)

    def appendS(self,synapse):
        self.listN.append(synapse)





