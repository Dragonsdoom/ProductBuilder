import Tkinter as tk

class invtItem(): 
    isUnique = False
    name = 'no name provided'
    description = 'no description provided'
    traits = {}

    def __init__(self,
                 name='no name provided',
                 description='no description provided'):
        self.setName(name)
        self.setDescription(description)

    def setUnique(self,isUnique):
        self.isUnique = isUnique
    def setName(self,name):
        self.name = name
    def setDescription(self,desc):
        self.description = desc

    def getTraits(self):
        return traits
        
    def updateTraitList(self,traitDict):
        for k,v in traitDict.items():
            self.traits[k] = v
    
class product(invtItem):
    def __init__(self, name='generic product',
                 description='no description provided'):
        invtItem.__init__(self, name, description)
        productTraits = {
            'marketValue':0, #estimated value of product
            'weight':0, #weight of product in kg
            'rarity':0, #rarity of product
            'features':0 #amount of special features
        }
        self.updateTraitList(productTraits)

class gun(product):
    def __init__(self,name='generic gun',
                 description='no description provided'):
        product.__init__(self,name,description)

        prodTraits = {
            'weight':3,
            'marketValue':100
        }
        self.updateTraitList(prodTraits)
        
        gunTraits = {
            'noise':0.5,
            'accuracy':0.5,
            'reliability':0.5,
            'power':0.5,
            'rateOfFire':0.5,
            'concealability':0.5,
            'stylishness':0.5,
            'ammoCapacity':0.5
        }
        self.updateTraitList(gunTraits)

def buildNewGun(name,description,traits):
    newGun = gun(name,description)
    newGun.updateTraitList(traits)
    return newGun

myGun = buildNewGun('AK-47','The universal boomstick',{'noise':0.75,'power':0.6, 'concealabilty':0.2})
print(myGun)
print(myGun.name)
print(myGun.description)
print(myGun.traits)
    

 
