class Database:
	def __init__(self) -> None:
		self.storage = {}


class Interface:
	PUT = 'put'
	GET = 'get'
	DELETE = 'delete'
	KEYS = 'keys'
	SEARCH = 'search'

	def __init__(self, database) -> None:
		# attach interface to database
		self.database = database.storage

	def run(self):
		while True:
			command = input("$ ")
			if command == 'exit':
				break
			command = command.split()  # split on spaces
			if len(command) < 1 or command[0] not in [self.PUT, self.GET, self.DELETE, self.SEARCH, self.KEYS]:
				print("Improper Command")
				continue
			method = command[0]
			data = command[1:]
			if self.PUT == method:
				key = data[0]
				value = data[1]
				self.put(key, value)
			elif self.GET == method:
				key = data[0]
				print(self.get(key))
			elif self.DELETE == method:
				key = data[0]
				self.delete(key)
			elif self.KEYS == method:
				print(self.keys())
			elif self.SEARCH == method:
				value = data[0]
				print(self.search(value))


	def get(self, key: str):
		'''
			Search for given key and returns it's value if present else return None.
			Same key but of different datatype are different (3 is not '3')
		'''
		return self.database.get(key, None)	# get is datatype sensitive 3 and '3' are different

	def put(self, key, value):
		'''
			Put a value against a key in the cache
			Create the entry if not present else update
		'''
		self.database[key] = value

	def delete(self, key):
		'''
			Remove a key if present
		'''
		if key in self.database:
			del self.database[key]

	def keys(self):
		'''
			Get all the keys in database
		'''
		return list(self.database.keys())

	def search(self, value):
		'''
			Search and return the key which have given value else return nothing
		'''
		return [k for k,v in self.database.items() if v == value]


if __name__ == "__main__":
	# provide 'exit' as input to stop the program
	database = Database()
	interface = Interface(database)
	interface.run()
