from dataStorage import dataStorageCPickle as dstorage
from inventoryItem import gun
from inventoryItemFactory import invItemFactory

class invItemController():
    ds = dstorage()
    def __init__(self,factory):
        self.factory = factory
        view = invItemView(self,factory)
        view.mainLoop()

    def createInvItem(self,cls,name,desc,unique,traits):
        self.factory.create(cls,name,desc,unique,traits)
        
    def storeInvItemsCreated(self):  
        self.ds.save(self.factory.getProdHistory(),'itemlist')

    def getInvItemsCreated(self):
        return self.factory.getProdHistory()
    
    def clearInvItemsCreated(self):
        self.factory.clearProdHistory()
