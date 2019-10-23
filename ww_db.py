import json

class database:
    data = {}
    nextUniqueID = 0

    def __init__(self):
        with open('db.json') as json_file:
            self.data = json.load(json_file)

    def save(self):
        print("Writing to Database....")
        with open('db.json', 'w+') as json_file:
            json.dump(self.data, json_file, indent=4, sort_keys=True)

    def add_item(self, name, w, h, description, category, warehouse_id, storedAt):
        
        self.data["warehouse"][warehouse_id-1]["items"].append({"id": self.nextUniqueID, "name": name, 
                                                                "width": w, "height": h, "description": description,
                                                                "category": category, "storedAt": storedAt, "itemCount": 0})

        self.data["warehouse"][warehouse_id-1]["storageLocation"][storedAt]["items"].append({"id": self.nextUniqueID, "name": name, 
                                                                "width": w, "height": h, "description": description,
                                                                "category": category})

        self.nextUniqueID = len(self.data["warehouse"][warehouse_id-1]["items"])

    def add_warehouse(self, h, w, l):
        print("Creating Warehouse....")

        warehouse_id = len(self.data["warehouse"]) + 1
        alpha = ['A', 'B', 'C', 'D']
        storageCap = ((w/5)*(h/5)*(l/5))
        cubicVolume = w*h*l

        self.data["warehouse"].append({"id": warehouse_id, "height": h, "length": l, "width": w, 
                                        "cubicVolume": cubicVolume, "items": [], "storageLocation": {}, "storageCap": storageCap})
        
        for i in range(0,4):
            for j in range(1,5):
                 self.data["warehouse"][warehouse_id-1]["storageLocation"].update({alpha[i]+str(j):{"remainingArea": "true", 
                                                                                                "items": []}})

    def get_item_list(self, warehouse_num):
        return self.data["warehouse"][warehouse_num-1]["items"]

    def get_warehouse_list(self):
        return self.data["warehouse"]

    def search_item_by_id(self, warehouse_num, id):
        for i in range(len(self.data["warehouse"][warehouse_num-1]["items"])):
            if(self.data["warehouse"][warehouse_num-1]["items"][i]["id"] == id):
                return self.data["warehouse"][warehouse_num-1]["items"][i]
    
    def search_item_by_name(self, warehouse_num, name):
        for i in range(len(self.data["warehouse"][warehouse_num-1]["items"])):
            if(self.data["warehouse"][warehouse_num-1]["items"][i]["name"] == name):
                return self.data["warehouse"][warehouse_num-1]["items"][i]

    def delete_item_by_id(self, warehouse_num, item_id):
        for i in range(len(self.data["warehouse"][warehouse_num-1]["items"])):
            if(self.data["warehouse"][warehouse_num-1]["items"][i]["id"] == item_id):
                self.nextUniqueID = item_id
                del self.data["warehouse"][warehouse_num-1]["items"][i]
                break
        
        print("Unable to find item by ID. Please try again.")

    def delete_item_by_name(self, warehouse_num, item_name):
        for i in range(len(self.data["warehouse"][warehouse_num-1]["items"])):
            if(self.data["warehouse"][warehouse_num-1]["items"][i]["name"] == item_name):
                del self.data["warehouse"][warehouse_num-1]["items"][i]
                self.nextUniqueID = i
                break
        
        print("Unable to find item by name. Please try again.")

    def delete_warehouse(self, warehouse_num):
        for i in range(len(self.data["warehouse"])):
            if(self.data["warehouse"][i]["id"] == warehouse_num):
                del self.data["warehouse"][i]
                self.reindex_warehouse()            
                break
        
        print("Unable to find warehouse by ID. Please try again.")

    # def reindex_items(self, warehouse_num):
    #     for i in range(len(self.data["warehouse"][warehouse_num]["items"])):
    #         self.data["warehouse"][warehouse_num]["items"]["id"] = i + 1
    #     self.dict_to_json("db")

    def reindex_warehouse(self):
        for i in range(len(self.data["warehouse"])):
                self.data["warehouse"][i]["id"] = i + 1
        # self.dict_to_json("db")

db1 = database()

db1.add_warehouse(500,500,500)

db1.save()

db1.add_item("toaster",50,50,"Tacos meant machine","electronic",1,"A1")

item = db1.search_item_by_name(1, "toaster")

db1.save()