__author__ = 'MisT'


class Node:
    def __init__(self, edges=[]):
        self.value = 0
        self.edges = edges

    def add(self, value):
        self.value += value

    def output(self):
        for e in self.edges:
            e.add(self.value)
        self.value = 0

