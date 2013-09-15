from dataStorage import dataStorageCPickle as dstorage
from inventoryItem import gun
from inventoryItemFactory import invItemFactory

class invItemController():
    factory = invItemFactory()
    ds = dstorage()

    def createInvItem(self,cls,name,desc,traits):
        self.factory.create(cls,name,desc,traits)
        
    def storeInvItemsCreated(self):  
        self.ds.save(self.factory.getProdHistory(),'itemlist')

    def getInvItemsCreated(self):
        return self.factory.getProdHistory()
    
    def clearInvItemsCreated(self):
        self.factory.clearProdHistory()
    
def printInvItemInfo(invItem):
    print(invItem)
    print(invItem.name)
    print(invItem.description)
    print(invItem.traits)
    print("\n")

def main():
    controller = invItemController()
    controller.createInvItem(gun,'AK-47','The universal boomstick',
                             {'power':0.6, 'accuracy':0.4 })

    for i in controller.getInvItemsCreated():
        printInvItemInfo(i)

main()    
