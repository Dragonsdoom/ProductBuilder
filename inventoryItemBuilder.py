from dataStorage import dataStorageCPickle as dstorage
from inventoryItem import gun
from inventoryItemFactory import invItemFactory

def storeInvItemsCreated(invItemList):
    ds = dstorage()
    ds.save(invItemList,'gunlist')

def printInvItemInfo(invItem):
    print(invItem)
    print(invItem.name)
    print(invItem.description)
    print(invItem.traits)
    print("\n")

def main():
    invItems = []
    factory = invItemFactory()
    iItem = factory.create(gun,'AK-47','The universal boomstick',
                           {'noise':0.75,'power':0.6, 'concealabilty':0.2})
    invItems.append(iItem)

    for i in invItems:
        printInvItemInfo(i)

main()
    
    
    
