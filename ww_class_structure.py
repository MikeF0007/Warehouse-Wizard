import numpy as np


class Item:
	def __init__(self, itemID, dimensions, name, description, storedAt):
		self.itemID = itemID  # unique integer ID assigned by the ID accumulator in the warehouse class
		self.dimensions = dimensions  # tuple of doubles that gives the height and width of the item
		self.name = name  # string variable containing the name of the item
		self.description = description  # string variable containing a brief description of that item
		self.storedAt = storedAt # tuple of integers holding

	# ----------------------------------------------------Methods----------------------------------------------------- #

	'''
	This function will return the item in a string format for outputting or saving purposes
	Parameters: None
	'''

class StorageSpace:
	def __init__(self, remainingArea, itemList, category=None, spaceLeft=True):
		# double value that holds the remaining area of available space
		self.remainingArea = remainingArea
		# string variable that can optionally be used to label the type of items stored there
		self.category = category
		# dictionary of items stored in this space. Key = unique id, value = item object
		self.itemList = itemList
		# boolean variable that is set to true when area == 0 and is false otherwise
		self.spaceLeft = spaceLeft

	# ----------------------------------------------------Methods----------------------------------------------------- #

	'''-----------------------------------------------------------------------------------------------------------------
	This function will place the item in the storage space by adding an entry to the dictionary and then subtracting its 
	area from the storage space.
	Parameters: i = Item to be stored and inserted in dictionary
	-----------------------------------------------------------------------------------------------------------------'''
	def storeItem(self, newItem):
		self.itemList[newItem.itemID] = newItem
		self.remainingArea = self.remainingArea - (newItem.dimensions[0] * newItem.dimensions[1])
		if self.remainingArea == 0:
			self.spaceLeft = False

	'''-----------------------------------------------------------------------------------------------------------------
	This removes the item specified by the unique id argument from the storage space dictionary and restores the area
	of that item. This should be called in conjunction with the warehouse function to maintain accurate warehouse state
	If item doesn't exist, then return False.
	Parameters: id = unique ID of the item to be removed
	-----------------------------------------------------------------------------------------------------------------'''
	def removeItem(self, uniqueID):
		self.remainingArea += (self.itemList[uniqueID].dimensions[0] * self.itemList[uniqueID].dimensions[1])
		self.itemList.pop(uniqueID)
		if not self.spaceLeft:
			self.spaceLeft = True

	'''-----------------------------------------------------------------------------------------------------------------
	This returns the item specified by the unique id argument from the storage space dictionary. If item doesn't exist,
	then return None
	Parameters: id = unique ID of the item to be retrieved
	-----------------------------------------------------------------------------------------------------------------'''
	def getItem(self, uniqueID):
		if uniqueID in self.itemList:
			return self.itemList[uniqueID]
		else:
			return None

	'''-----------------------------------------------------------------------------------------------------------------
	This returns a list of items specified by the item name argument from the storage space dictionary. If no items of
	of that name exist, then return None
	Parameters: itemName = string that describes the item to be returned
	-----------------------------------------------------------------------------------------------------------------'''
	def getAllItems(self):
		items = []
		for item in self.itemList.values():
			items.append(item)
		return items


class Warehouse:

	def __init__(self, filename, dimensions = (1000, 1000), manifest={}, items=0, storageSpaces=None, numSpaces=16, id=0):
		# string filename of the warehouse to be used for read and write functions
		self.filename = filename
		# pair of doubles that gives the height and width of the warehouse. Dictates the area of storage spaces
		self.dimensions = dimensions
		# integer number of items in the warehouse for ease of use
		self.itemCount = items
		# integer number of storage spaces in matrix that have a remaining area value > 0
		self.numOpenSpaces = numSpaces
		# integer accumulator that is given to an item as its unique ID upon creation and subsequently incremented
		self.nextUniqueID = id
		# pair of doubles that gives the maximum dimensions for every storage (all size)
		self.storageCap = (dimensions[0]/5) * (dimensions[1]/5)
		# matrix of StorageSpace objects (list of storage space lists)
		if storageSpaces is None:
			self.spaceMatrix = [[StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict())],
								[StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict())],
								[StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict())],
								[StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict()), StorageSpace(self.storageCap, dict())]]
		else:
			self.spaceMatrix = storageSpaces
	# ----------------------------------------------------Methods----------------------------------------------------- #

	'''-----------------------------------------------------------------------------------------------------------------
	This function will be called by the application function and be passed all the parameters for the new item
	to be added to the list. This function within the warehouse will create the item and assign it a unique ID,
	passing these parameters to the Item constructor. This function will then find the next available space in the
	warehouse. If an error occurs, this will be printed out and we will back out. Otherwise, the item will be inserted
	using the returned coordinates. If unsuccessful, return False
	Parameters: self explanatory item information
	-----------------------------------------------------------------------------------------------------------------'''
	def addItem(self, dimensions, name, description="", category=None):
		availableSpot = self.findAvailableSpot(dimensions, category)
		if availableSpot is not None:
			newItem = Item(itemID=self.nextUniqueID, dimensions=dimensions, name=name, description=description, storedAt=availableSpot)
			self.spaceMatrix[availableSpot[0]][availableSpot[1]].storeItem(newItem)
			self.nextUniqueID += 1
			self.itemCount += 1
			return availableSpot
		else:
			return None

	'''-----------------------------------------------------------------------------------------------------------------
	This function will remove an item from the warehouse if it exists (using the warehouse's search function). The 
	warehouse spaces will be sequentially scanned, and will have their dictionaries checked against the ID. If the item 
	is found, that item's area will be added back to the storage space and then be removed from that storage space's 
	dictionary. The storage location of that item
	Parameter: id = integer of unique ID number
	-----------------------------------------------------------------------------------------------------------------'''
	def removeItem(self, uniqueID):
		item = self.searchByID(uniqueID)
		if item is not None:
			self.spaceMatrix[item.storedAt[0]][item.storedAt[1]].removeItem(uniqueID)
			self.itemCount -= 1
			return item
		return None

	'''-----------------------------------------------------------------------------------------------------------------
	This function will search for and return the the item by using the warehouse's dictionary. Otherwise, return None
	Parameter: id = integer of unique ID number
	-----------------------------------------------------------------------------------------------------------------'''
	def searchByID(self, uniqueID):
		for row in self.spaceMatrix:
			for space in row:
				if uniqueID in space.itemList.keys():
					return space.itemList[uniqueID]
		return None

	'''-----------------------------------------------------------------------------------------------------------------
	This function will search for and return a list of coordinate item name pairs sequentially looking through the
	stoarage spaces. Otherwise, return empty list if no items of the given name can be found
	Parameter: name = name of the item
	-----------------------------------------------------------------------------------------------------------------'''
	def searchByName(self, name):
		nameListAllSpaces = []
		for row in self.spaceMatrix:
			for space in row:
				nameListCurSpace = []
				for id, item in space.itemList.items():
					if item.name == name:
						nameListCurSpace.append(item)
				if len(nameListCurSpace) != 0:
					nameListAllSpaces.append(nameListCurSpace)
		if len(nameListAllSpaces) == 0:
			return None
		return nameListAllSpaces

	'''-----------------------------------------------------------------------------------------------------------------
	This function will search for and return a list of storage spaces with a matching category type. Otherwise, return 
	an empty list ito spaces have the given category name
	Parameter: name = name of the item
	-----------------------------------------------------------------------------------------------------------------'''
	def searchByCategory(self, category):
		i = 0
		catList = []
		for row in self.spaceMatrix:
			j = 0
			for space in row:
				if category is not None and category == space.category:
					catList.append([i, j])
				j = j + 1
			i = i + 1
		if len(catList) == 0:
			return None
		return catList

	'''-----------------------------------------------------------------------------------------------------------------
	This function sequentially looks through the available storage space and returns a pair of coordinates
	to the available storage that has space and also matches the specified category. If a category cannot be found,
	then the program will scan for an empty storage space and if it finds one, then assign that storage space the
	category label and the coordinates for that location will be returned. Otherwise, the system will return an None
	If the category is None, then the system will return the first available uncategorized storage space. If all spaces
	are labeled, None will be returned.
	Parameter: location = pair that contains the coordinates in the space matrix. Can be type None
	-----------------------------------------------------------------------------------------------------------------'''
	def findAvailableSpot(self, dimensions, category=None):
		if category is not None:
			i = 0
			for row in self.spaceMatrix:
				j = 0
				for space in row:
					if category == space.category and space.spaceLeft and (space.remainingArea - (dimensions[0] * dimensions[1])) >= 0:
						return [i, j]
					j = j + 1
				i = i + 1

		# We weren't able to find a storage space designated for that category or no category was specified
		i = 0
		for row in self.spaceMatrix:
			j = 0
			for space in row:
				if space.category is None and space.spaceLeft and (space.remainingArea - (dimensions[0] * dimensions[1])) >= 0:
					return [i, j]
				j = j + 1
			i = i + 1
		return None
