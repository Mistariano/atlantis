__author__ = 'MisT'


from pymongo import MongoClient


connect=MongoClient().atlantis
current=connect['current']
geneBase=connect['gene']
structBase=connect['structure']

def saveStruct(info):
    structBase.insert(info)

def saveGene(info):
    geneBase.insert(info)

def saveCurrent(info):
    current.drop()
    for i in info:
        current.insert(i)

def drop():
    print'Are you sure to DROP ?'
    x=input('Input \'6\':')
    while x!=6:
        x=input('Input \'6\':')
    structBase.drop()
    geneBase.drop()
    current.drop()