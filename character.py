class character(): 
    isUnique = False
    name = 'no name provided'
    description = 'no description provided'
    traits = {
        'happiness':0.5,
        'assertiveness':0.5,
        'wealthiness':0.5,
        'patience':0.5,
        'marketknowledge':0,
        'insiderknowledge':0,
        'violence':0,
        'toughness':0.5
    }

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
