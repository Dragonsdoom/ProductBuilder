from traitObject import traitObject as tO

class character(tO):
    def __init__(self,
                 name='no name provided',
                 description='no description provided'):
        tO.__init__(name,description)
        charTraits = {
                'happiness':0.5,
                'assertiveness':0.5,
                'patience':0.5,
                'violence':0,
                'toughness':0.5
            }
        self.updateTraitList(charTraits)

class customer(character):
    def __init__(self,
                 name='no name provided',
                 description='no description provided'):
        character.__init__(name,description)
        custTraits = {
                'wealthiness':0.5,
                'marketknowledge':0,
                'insiderknowledge':0,
            }
        self.updateTraitList(charTraits)
