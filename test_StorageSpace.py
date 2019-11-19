import unittest
from ww_class_structure import StorageSpace, Item


class TestStorageSpace(unittest.TestCase):
    def setUp(self):
        self.ss_1 = StorageSpace(40000, dict())
        self.item_1 = Item(0, (40000, 1), "Boombox", "loud", (0, 0))
        self.item_2 = Item(1, (1000, 1), "Guitar", "6-string", (0, 0))
        self.item_3 = Item(2, (2000, 1), "Xbox One", "original", (0, 0))

        self.ss_2 = StorageSpace(0, {0: self.item_1})

    def test_storeItem(self):
        self.ss_1.storeItem(self.item_1)

        self.assertNotEqual(len(self.ss_1.itemList), 0)
        self.assertEqual(self.ss_1.itemList[0], self.item_1)
        self.assertEqual(self.ss_1.spaceLeft, False)

    def test_removeItem(self):
        self.ss_2.removeItem(0)

        self.assertEqual(self.ss_2.remainingArea, 40000)
        self.assertEqual(len(self.ss_2.itemList), 0)
        self.assertEqual(self.ss_2.spaceLeft, True)

    def test_getItem(self):
        self.assertEqual(self.ss_2.getItem(0), self.item_1)
        self.assertIsNone(self.ss_1.getItem(0))

    def test_getAllItems(self):
        self.ss_1.storeItem(self.item_2)
        self.ss_1.storeItem(self.item_3)

        self.assertEqual(self.ss_1.getAllItems(), [self.item_2, self.item_3])


if __name__ == '__main__':
    unittest.main()