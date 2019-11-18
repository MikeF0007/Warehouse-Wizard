import unittest
from ww_db import *

class TestDB(unittest.TestCase):
    
    def test_init_new_file(self):
        db = database("unittest")
        self.assertEqual(os.path.isfile('unittest.json'), True)
    
    def test_fileSize(self):
        db = database("unittest")
        oldFileSize = os.path.getsize("unittest.json")

        warehouse_changes = db.load()
        itemName = "unittest#" + str(warehouse_changes.itemCount)
        warehouse_changes.addItem((20,20),itemName)
        db.save(warehouse_changes)

        warehouse_test = db.load()

        newFileSize = os.path.getsize("unittest.json")

        #Checking file size difference
        self.assertGreater(newFileSize, oldFileSize)

    def test_get_warehouse_list(self):
        db = database("unittest")
        whlist = db.get_warehouse_list()
        print(whlist)

        whlistLen = len(whlist)

        #adding to warehouse list to see if it works
        db2 = database("unittest" + str(whlistLen + 1))
        newWarehouseObj = Warehouse("unittest" + str(whlistLen + 1))
        db2.save(newWarehouseObj)
        whlist2 = db2.get_warehouse_list()
        print(whlist2)

        whlist2Len = len(whlist2)

        self.assertEqual(whlistLen + 1, whlist2Len)


if __name__ == '__main__':
    unittest.main()