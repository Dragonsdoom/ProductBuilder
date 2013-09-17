class traitObject():
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
