import inventoryItemController as iiController
import inventoryItemFactory as iiFactory

def main():
    controller = iiController(iiFactory())
    #controller.createInvItem(gun,'AK-47','The universal boomstick',False,
                             #{'power':0.6, 'accuracy':0.4})

main() 
