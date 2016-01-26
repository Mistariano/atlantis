__author__ = 'MisT'

from specie import Specie

class Nature:
    def __init__(self,firstSpecie):
        self.species=[firstSpecie]
        self.generation=1

    def loop(self):
        print'new generation ^_^'
        print'generation:',self.generation
        newSpecies=[]
        for s in self.species:
            for n in s.loop():
                newSpecies.append(n)
        for n in newSpecies:
            self.species.append(Specie(firstMember=n))
        self.generation+=1



