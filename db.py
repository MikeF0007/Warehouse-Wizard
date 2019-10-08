import json

class db:
    data = {}

    def __init__(self):
        with open('db.json') as json_file:
            self.data = json.load(json_file)

    def dict_to_json(self, type):
        with open(type + '.json', 'w+') as json_file:
            json.dump(self.data, json_file, indent=4, sort_keys=True)

    def add_item(self, name, w, h, description, category, warehouse_num):
        item_id = len(self.data["warehouse"][warehouse_num-1]["items"])
        self.data["warehouse"][warehouse_num-1]["items"].append({"id": item_id, "name": name, 
                                                                "width": w, "height": h, "description": description,
                                                                "category": category})
        self.dict_to_json("db")

    def add_warehouse(self, w, l):
        warehouse_id = len(self.data["warehouse"]) + 1
        alpha = ['A', 'B', 'C', 'D']

        self.data["warehouse"].append({"id": warehouse_id, "length": l, "width": w, "items": [], "storage_loc":{}})
        
        for i in range(0,4):
            for j in range(1,5):
                 self.data["warehouse"][warehouse_id-1]["storage_loc"].update({alpha[i]+str(j):{}})

        self.dict_to_json("db")

    def get_item_list(self, warehouse_num):
        return self.data["warehouse"][warehouse_num-1]["items"]

    def get_warehouse_list(self):
        return self.data["warehouse"]

    def delete_item_by_id(self, warehouse_num, item_id):
        for i in range(len(self.data["warehouse"][warehouse_num-1]["items"])):
            if(self.data["warehouse"][warehouse_num-1]["items"][i]["id"] == item_id):
                del self.data["warehouse"][warehouse_num-1]["items"][i]
                self.reindex_items(warehouse_num)
                break
        
        print("Unable to find item by ID. Please try again.")

    def delete_item_by_name(self, warehouse_num, item_name):
        for i in range(len(self.data["warehouse"][warehouse_num-1]["items"])):
            if(self.data["warehouse"][warehouse_num-1]["items"][i]["name"] == item_name):
                del self.data["warehouse"][warehouse_num-1]["items"][i]
                self.reindex_items(warehouse_num)
                break
        
        print("Unable to find item by name. Please try again.")

    def delete_warehouse(self, warehouse_num):
        for i in range(len(self.data["warehouse"])):
            if(self.data["warehouse"][i]["id"] == warehouse_num):
                del self.data["warehouse"][i]
                self.reindex_warehouse()            
                break
        
        print("Unable to find warehouse by ID. Please try again.")

    def reindex_items(self, warehouse_num):
        for i in range(len(self.data["warehouse"][warehouse_num]["items"])):
                self.data["warehouse"][warehouse_num]["items"]["id"] = i + 1
        self.dict_to_json("db")

    def reindex_warehouse(self):
        for i in range(len(self.data["warehouse"])):
                self.data["warehouse"][i]["id"] = i + 1
        self.dict_to_json("db")

db1 = db()

db1.add_warehouse(500,500)
