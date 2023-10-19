class Player(object):
	def __init__(self, name, place, backpack):
		self.name = name
		self.place = place
		self.backpack = []

	def look(self):
		self.place.look()

	def go_to(self, location):
		if type(location) != str:
			print("Place must be a string")
			return
		destination_place = self.place.get_neighbor(location)
		if destination_place != self.place:
			self.unlock(destination_place)
			if not(destination_place.locked):
					print('You go to ', location)
					self.place = destination_place


	def talk_to(self, person):
		if type(person) != str:
			print('Person has to be a string.') 
		if person not in self.place.characters:
			print(person, 'is not at your location. Try looking around to see who is.' )
		else:
			character = self.place.characters[person]
			print()
			print(character.name, 'says' , character.message)


	def take(self, thing):
		if type(thing) != str:
			print('Thing should be a string.')
		if thing not in self.place.things:
			print(thing, 'is not at your location. Try looking around to see what is')
		else:
			item = self.place.things[thing]
			print (thing, 'is added to inventory')
			self.backpack += [item]
			self.place.take(item.name)
        	

	def check_backpack(self):
		print('In your backpack:')
		if not self.backpack:
			print('there is nothing.')
		else:
			for item in self.backpack:
				print('	', item.name, '-', item.description)
		return [item.name for item in self.backpack]

	def unlock(self, place):
		if place.locked and 'helicopter' not in [item.name for item in self.backpack]:
			print('You need a helicopter to get there safely.')
		elif not(place.locked):
			return
		else:
			place.locked = False
			print ('You get in the helicopter.')


class Character(object):
	def __init__(self, name, message):
		self.name = name
		self.message = message

	def talk(self):
		return self.message


class Thing(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def use(self, place):
		print("You can't use a {0} here".format(self.name))


class Place(object):
	def __init__(self, name, description, characters, things, locked):
		self.name = name
		self.description = description
		self.characters = {character.name: character for character in characters}
		self.things = {thing.name: thing for thing in things}
		self.exits = {} # {'name': (exit, 'description')}
		self.locked = locked

	def look(self):
		print('You are currently at ' + self.name + '. ' +self.description)
		print('You take a look around and see:')
		print('Characters:')
		if not self.characters:
			print('	no one in particular')
		else:
			for character in self.characters:
				print('	', character)
		print('Things:')
		if not self.things:
			print('	nothing in particular')
		else:
			for thing in self.things.values():
				print('	', thing.name, '-', thing.description)
		self.check_exits()

	def get_neighbor(self, exit):
		if type(exit) != str:
			print('Exit has to be a string.')
			return self
		elif exit in self.exits:
			exit_place = self.exits[exit][0]
			return exit_place
		else:
			print("Can't go to {} from {}.".format(exit, self.name))
			print("Try looking around to see where to go.")
			return self

	def take(self, thing):
		return self.things.pop(thing)

	def check_exits(self):
		print('You can exit to:')
		for exit in self.exits:
			print('	', exit)

	def add_exits(self, places):
		for place in places:
			self.exits[place.name] = (place, place.description)