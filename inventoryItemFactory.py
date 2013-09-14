from inventoryItem import invItem

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
