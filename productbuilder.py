import Tkinter as tk

class invItem(): 
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
    
class product(invItem):
    def __init__(self, name='generic product',
                 description='no description provided'):
        invItem.__init__(self, name, description)
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

class invItemFactory():
    prodHistory = []
    
    def create(self, cls=invItem, name='no name provided',
                 description='no description provided',unique=False,traitDict={}):
        if not issubclass(cls,invItem):
            raise TypeError('class provided is not subclass of inventory item')
        iItem = cls(name,description)
        iItem.isUnique = unique
        iItem.updateTraitList(traitDict)
        self.prodHistory.append(iItem)
        return iItem
    
    def last(self,cls=invItem,back=0,name=None):
        if not issubclass(cls,invItem):
            raise TypeError('class provided is not subclass of inventory item')
        retValue = self.prodHistory
        retValue = [x for x in retValue if issubclass(cls,invItem)]
        if name:
            retValue = [x for x in retValue if x.name == name]
        return self.prodHistory[len(self.prodHistory)-1-back]

factory = invItemFactory()
factory.create(gun,'AK-47','The universal boomstick',{'noise':0.75,'power':0.6, 'concealabilty':0.2})
myGun = factory.last()
print(myGun)
print(myGun.name)
print(myGun.description)
print(myGun.traits)
    

 
