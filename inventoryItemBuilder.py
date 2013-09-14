from inventoryItem import gun
from inventoryItemFactory import invItemFactory

factory = invItemFactory()
factory.create(gun,'AK-47','The universal boomstick',{'noise':0.75,'power':0.6, 'concealabilty':0.2})
myGun = factory.last()
print(myGun)
print(myGun.name)
print(myGun.description)
print(myGun.traits)
