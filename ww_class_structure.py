import numpy as np


class Item:
	def __init__(self, itemID, dimensions, name, description):
		self.itemID = itemID  # unique integer ID assigned by the ID accumulator in the warehouse class
		self.dimensions = dimensions  # tuple of doubles that gives the height and width of the item
		self.name = name  # string variable containing the name of the item
		self.description = description  # string variable containing a brief description of that item

	# ----------------------------------------------------Methods----------------------------------------------------- #

	'''
	This function will return the item in a string format for outputting or saving purposes
	Parameters: None
	'''
	def toString(self):
		return "Item ID: {}\nName: {}\nDescription: {}\nDimensions: {} x {}\n".format(self.itemID, self.name,
																					  self.description,
																					  self.dimensions[0],
																					  self.dimensions[1])


class StorageSpace:
	def __init__(self, remainingArea, itemList={}, category=None, spaceLeft=True):
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
		self.itemList.pop(uniqueID)
		self.remainingArea = self.remainingArea + (self.itemList[uniqueID].dimensions[0] * self.itemList[uniqueID].dimensions[1])
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


class Warehouse:

	def __init__(self, manifest={}, items=0, storageSpaces=None, numSpaces=16, dimensions=(250, 250), id=0):
		# dictionary where keys are item names (string) and values are dictionaries mapping storage location to # of occurrences
		self.itemManifest = manifest
		# integer number of items in the manifest for ease of use
		self.itemCount = items
		# integer number of storage spaces in matrix that have a remaining area value > 0
		self.numOpenSpaces = numSpaces
		# pair of doubles that gives the height and width of the warehouse. Dictates the area of storage spaces
		self.dimensions = dimensions
		# integer accumulator that is given to an item as its unique ID upon creation and subsequently incremented
		self.nextUniqueID = id
		# pair of doubles that gives the maximum dimensions for every storage (all size)
		self.storageCap = (dimensions[0]/5) * (dimensions[1]/5)
		# matrix of StorageSpace objects (list of storage space lists)
		if storageSpaces is None:
			self.spaceMatrix = [[StorageSpace(self.storageCap)]*4]*4
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
		newItem = Item(itemID=self.nextUniqueID, dimensions=dimensions, name=name, description=description)
		availableSpot = self.findAvailableSpot(newItem.dimensions, category)
		if availableSpot is None:
			pass
			# ERROR
		else:
			self.itemManifest[newItem.name][availableSpot] += 1
			self.spaceMatrix.item((availableSpot[0], availableSpot[1])).storeItem(newItem)
			# SUCCESS

	'''-----------------------------------------------------------------------------------------------------------------
	This function will remove an item from the warehouse if it exists (search using warehouse's dictionary. The 
	warehouse spaces will be sequentially scanned, and will have their dictionaries checked against the ID. If the item 
	is found, that item's area will be added back to the storage	space and then be removed from that storage space's 
	dictionary. If unsuccessful, return False.
	Parameter: id = integer of unique ID number
	-----------------------------------------------------------------------------------------------------------------'''
	def removeItem(self, uniqueID):
		itemLocation = self.searchItem(uniqueID)
		if itemLocation is not None:
			self.spaceMatrix.item((itemLocation[0], itemLocation[1])).removeItem(uniqueID)
			return True
		else:
			return False
		# ERROR

	'''-----------------------------------------------------------------------------------------------------------------
	This function will search for and return the coordinates to the storage location containing the item by using the
	warehouse's dictionary. Otherwise, return empty list
	Parameter: id = integer of unique ID number
	-----------------------------------------------------------------------------------------------------------------'''
	def searchItem(self, uniqueID):
		i = j = 0
		for row in self.spaceMatrix:
			for space in row:
				if uniqueID in space.itemList:
					return [i, j]
				j = j + 1
			i = i + 1
		return None

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
			i = j = 0
			for row in self.spaceMatrix:
				for space in row:
					if category == space.category and space.spaceLeft \
						and (self.remainingArea - (dimensions[0] * dimensions[1])) >= 0:
						return [i, j]
					j = j + 1
				i = i + 1

		# We weren't able to find a storage space designated for that category or no category was specified
		i = j = 0
		for row in self.spaceMatrix:
			for space in row:
				if space.category is None and space.spaceLeft:
					return [i, j]
				j = j + 1
			i = i + 1
		return None


# --------------------------------------------------Global Functions-------------------------------------------------- #

'''---------------------------------------------------------------------------------------------------------------------
Prompt the user in UI to get the item information and then invoke/pass this information to backend functions. Details
of the item's new storage location or notification of failure will be output to the bottom window.
---------------------------------------------------------------------------------------------------------------------'''
def addItem():
	pass


'''---------------------------------------------------------------------------------------------------------------------
Prompt the user in UI to enter item name or item id. If the id is entered, then this will be passed to backend functions
and immediately be removed with a notice printing in the bottom window. If the name of the item is entered, a list of 
items with their ID's and storage locations will be printed in the item window, and the bottom window will ask the user 
to enter the ID of the item they would like to remove. Then proceed as usual with the entered ID. Indication of success 
or failure will be output to the bottom window.
---------------------------------------------------------------------------------------------------------------------'''
def removeItem():
	pass


'''---------------------------------------------------------------------------------------------------------------------
This will have a few variants. The first would be if the user were to enter an item ID. Here, we would simply pass this
to the backend search funtions and then if the search is successful, the item information and location will be printed
in the item window. If the user enter the name of the item, then the storage spaces will be sequentially searched and,
all items matching that name will be appended to a list. This list will then be output to the item window. For all 
unsuccessful cases, a error message will be displayed in bottom window.
---------------------------------------------------------------------------------------------------------------------'''
def searchItem():
	pass


'''---------------------------------------------------------------------------------------------------------------------
This will load first prompt the user to save if they are curently working on an unsaved project. Then the objects in the 
backend will be cleared and then read into and populated from an external DB. The UI will also be cleared and redrawn.
---------------------------------------------------------------------------------------------------------------------'''
def loadWarehouse():
	pass


'''---------------------------------------------------------------------------------------------------------------------
This will write the objects in the backend to an external DB.
---------------------------------------------------------------------------------------------------------------------'''
def saveWarehouse():
	pass


'''---------------------------------------------------------------------------------------------------------------------
This will prompt the user to save if they are currently working on an unsaved warehouse. Subsequently, the objects in 
the backend will be cleared and so will the UI
---------------------------------------------------------------------------------------------------------------------'''
def newWarehouse():
	pass


'''---------------------------------------------------------------------------------------------------------------------
This will redraw the UI whenever changes are made/functions have terminated
---------------------------------------------------------------------------------------------------------------------'''
def updateDisplay():
	pass


'''---------------------------------------------------------------------------------------------------------------------
This function prompts the user to select a storage space to set aside for a category of items of their choosing. UI 
elements will retrieve input from the user which will be passed to the warehouse object, where it will update the
category of the selected space
---------------------------------------------------------------------------------------------------------------------'''
def setCategory():
	pass


'''---------------------------------------------------------------------------------------------------------------------
This function will get the encoded integer index for the given row label (A, B, C, D)
Parameters: rowLabel = the character label for the row of a storage location
---------------------------------------------------------------------------------------------------------------------'''
def getEncoding(rowLabel):
	if rowLabel == 'A':
		return 0
	elif rowLabel == 'B':
		return 1
	elif rowLabel == 'C':
		return 2
	else:
		return 3
