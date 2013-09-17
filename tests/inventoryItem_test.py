import unittest as ut
from productbuilder.inventoryItem import invItem

class TestInventoryItem(ut.TestCase):
    def setUp(self):
        self.invItem = invItem()
        pass
    def test_updateTraitList_param_accepts_dict(self):
        self.assertTrue(self.invItem.updateTraitList({'trait':0}))
    def test_updateTraitList_param_denies_empty_dict(self):
        self.assertTrue(False)
    def test_updateTraitList_param_only_accepts_dict(self):
        self.assertTrue(False)

if __name__ == '__main__':
    ut.main()
