import unittest
from ww_class_structure import Warehouse, StorageSpace, Item


class TestWarehouse(unittest.TestCase):
    def setUp(self):
        # empty warehouse
        self.wh_1 = Warehouse("wh_1", (1000, 1000))

        # warehouse with 1 item
        self.item_1 = Item(0, (40000, 1), "Boombox", "loud", (0, 0))
        self.item_2 = Item(1, (100, 1), "Guitar", "6-string", (0, 1))
        self.wh_2 = Warehouse("wh_2", (1000, 1000), items=2, id=2)
        self.customMatrix = [[StorageSpace(self.wh_2.storageCap, {0: self.item_1}), StorageSpace(self.wh_2.storageCap, {1: self.item_2}),
                              StorageSpace(self.wh_2.storageCap, dict()), StorageSpace(self.wh_2.storageCap, dict())],
                             [StorageSpace(self.wh_2.storageCap, dict()), StorageSpace(self.wh_2.storageCap, dict()),
                              StorageSpace(self.wh_2.storageCap, dict()), StorageSpace(self.wh_2.storageCap, dict())],
                             [StorageSpace(self.wh_2.storageCap, dict()), StorageSpace(self.wh_2.storageCap, dict()),
                              StorageSpace(self.wh_2.storageCap, dict()), StorageSpace(self.wh_2.storageCap, dict())],
                             [StorageSpace(self.wh_2.storageCap, dict()), StorageSpace(self.wh_2.storageCap, dict()),
                              StorageSpace(self.wh_2.storageCap, dict()), StorageSpace(self.wh_2.storageCap, dict())]]
        self.customMatrix[0][0].remainingArea = 0
        self.customMatrix[0][0].spaceLeft = False
        self.customMatrix[0][1].category = "Instruments"
        self.wh_2.spaceMatrix = self.customMatrix
        pass

    def test_findAvailableSpot(self):
        self.assertIsNone(self.wh_1.findAvailableSpot((40001, 1)))
        self.assertEqual(self.wh_1.findAvailableSpot((40000, 1)), [0, 0])

        self.assertEqual(self.wh_2.findAvailableSpot((1, 1)), [0, 2])
        self.wh_2.spaceMatrix[0][2].category = "Games"
        self.assertEqual(self.wh_2.findAvailableSpot((1, 1)), [0, 3])
        self.assertEqual(self.wh_2.findAvailableSpot((1, 1), "Instruments"), [0, 1])
        self.assertEqual(self.wh_2.findAvailableSpot((1, 1), "Random"), [0, 3])

    def test_addItem(self):
        self.wh_1.addItem((40000, 1), "Boombox", "loud", None)

        self.assertEqual(len(self.wh_1.spaceMatrix[0][0].itemList), 1)
        self.assertEqual(self.wh_1.spaceMatrix[0][0].itemList[0].name, "Boombox")
        self.assertEqual(self.wh_1.nextUniqueID, 1)
        self.assertEqual(self.wh_1.itemCount, 1)

    def test_removeItem(self):
        self.wh_2.removeItem(0)

        self.assertEqual(len(self.wh_2.spaceMatrix[0][0].itemList), 0)
        self.assertEqual(self.wh_2.nextUniqueID, 2)
        self.assertEqual(self.wh_2.itemCount, 1)

    def test_searchByID(self):
        self.assertEqual(self.wh_2.searchByID(0), self.item_1)
        self.assertIsNone(self.wh_2.searchByID(5))

    def test_searchByName(self):
        self.assertEqual(self.wh_2.searchByName("Boombox"), [[self.item_1]])
        self.assertIsNone(self.wh_2.searchByName("Yoyo"))

    def test_searchByCategory(self):
        self.assertEqual(self.wh_2.searchByCategory("Instruments"), [[0, 1]])
        self.assertIsNone(self.wh_2.searchByCategory("Computers"))


if __name__ == '__main__':
    unittest.main()
