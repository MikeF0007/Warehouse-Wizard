import json
from ww_class_structure import Warehouse, StorageSpace, Item
import os.path
from os import path
import time


class database:
    data = {}
    newData = {}
    warehouseList = {}
    nextUniqueID = 0

    def __init__(self, filename):
        if path.exists(filename + ".json"):
            with open(filename + '.json') as json_file:
                self.data = json.load(json_file)
        else:
            with open(filename + '.json', 'a+') as json_file:
                json.dump({
                    "warehouse": []
                }, json_file, indent=4, sort_keys=True)
                json_file.close()

            with open(filename + '.json') as json_file:
                self.data = json.load(json_file)
                json_file.close()

        with open('warehouselist.json') as json_file:
            self.warehouseList = json.load(json_file)
            json_file.close()

    def save(self, warehouse):
        print("Writing to Database....")
        self.warehouseObj = warehouse

        self.newData = {u'warehouse': []}
        self.add_warehouse(self.warehouseObj)

        with open(self.warehouseObj.filename + '.json', 'w') as json_file:
            json.dump(self.newData, json_file, indent=4, sort_keys=True)

        with open('warehouseList.json', 'w+') as json_file:
            json.dump(self.warehouseList, json_file, indent=4, sort_keys=True)

    def load(self):
        alpha = ['A', 'B', 'C', 'D']
        self.warehouseObjLoad = Warehouse(self.data["warehouse"][0]["filename"],
                                          (self.data["warehouse"][0]["height"], self.data["warehouse"][0]["width"]))

        self.warehouseObjLoad.itemCount = self.data["warehouse"][0]["itemCount"]
        self.warehouseObjLoad.storageCap = self.data["warehouse"][0]["storageCap"]

        for i in range(0, 4):
            for j in range(1, 5):
                index = alpha[i] + str(j)
                itemList = self.data["warehouse"][0]["storageLocation"][index]["items"]

                for k in range(len(itemList)):
                    self.warehouseObjLoad.addItem((itemList[k]["dimensions"][0], itemList[k]["dimensions"][1]),
                                                  itemList[k]["name"], itemList[k]["description"])

        return self.warehouseObjLoad

    def add_warehouse(self, warehouse):
        print("Creating Warehouse....")

        duplicate = False

        if len(self.warehouseList["warehouseList"]) == 0:
            print("I DID THIS")
            self.warehouseList["warehouseList"].append(warehouse.filename)
        else:
            for i in self.warehouseList["warehouseList"]:
                if i == warehouse.filename:
                    duplicate = True

            if duplicate == False:
                self.warehouseList["warehouseList"].append(warehouse.filename)

        alpha = ['A', 'B', 'C', 'D']

        self.newData["warehouse"].append(
            {"filename": warehouse.filename, "height": warehouse.dimensions[0], "width": warehouse.dimensions[1],
             "storageCap": warehouse.storageCap, "itemCount": warehouse.itemCount, "storageLocation": {},
             "nextUniqueID": warehouse.nextUniqueID})

        for i in range(0, 4):
            for j in range(1, 5):
                self.newData["warehouse"][0]["storageLocation"].update({alpha[i] + str(j): {
                    "remainingArea": warehouse.spaceMatrix[i][j - 1].remainingArea,
                    "category": warehouse.spaceMatrix[i][j - 1].category,
                    "items": [], "spaceLeft": warehouse.spaceMatrix[i][j - 1].spaceLeft}})

                newItemList = warehouse.spaceMatrix[i][j - 1].getAllItems()
                index = alpha[i] + str(j)

                for k in range(len(newItemList)):
                    self.newData["warehouse"][0]["storageLocation"][index]["items"].append(
                        {"itemID": newItemList[k].itemID, "dimensions": newItemList[k].dimensions,
                         "name": newItemList[k].name, "description": newItemList[k].description})

    def get_warehouse_list(self):
        list = []
        for i in self.warehouseList["warehouseList"]:
            list.append(i)
        return list


db = database("Test")
# newWarehouseObj = db.load()
# newWarehouseObj.filename = "Test"
# newWarehouseObj.addItem((20,20),"TestNew")
# newWarehouseObj.addItem((20,20),"TestNew2")


# checklist = db.get_warehouse_list()

# print(type(checklist))
# print(checklist)

