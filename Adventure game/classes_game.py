# A "simple" adventure game.

class Player(object):
	def __init__(self, name, place, backpack):
		self.name = name
		self.place = place
		self.backpack = backpack
    

	def look(self):
		self.place.look()

	def go_to(self, location):
		if not(location in self.place.exits):
			print('You cannot go from', self.place.name, 'to',  location, '.Try looking around to see where to go' )
		else:
			location.unlock()
			print('You go to ', location)
			self.place = location 


	def talk_to(self, person):
		print(self.place.characters)
		if not(self.place.characters[person] in self.place.characters):
			print(person, 'is not at your location. Try looking around to see who is.' )
		else:
			print()
			print(person.name, '-', person.message)


	def take(self, thing):
		if not(thing in self.place.things):
			print('There is no such item at your location. Try looking around.')
		elif thing in backpack:
			print(thing, 'already in backpack')
		else:
			print ('you take', thing)
			backpack += [thing]
        

	def check_backpack(self):
		print('In your backpack:')
		if not self.backpack:
			print('    there is nothing.')
		else:
			for item in self.backpack:
				print('   ', item.name, '-', item.description)



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


class Place(object):
	def __init__(self, name, description, characters, things, locked):
		self.name = name
		self.description = description
		self.characters = {character.name: character for character in characters}
		self.things = {thing.name: thing for thing in things}
		self.locked = False
		self.exits = {}

	def look(self):
		print('You are currently at ', self.name, '. ', self.description + '. You take a look around and see:')
		print('Characters:')
		if len(self.characters) == 0:
			print('no one in particular')
		else:
			for character in self.characters:
				print(character.name)
		print('Things:')
		if len(self.things) == 0:
			print('nothing in particular')
		else:
			for thing in self.things.values():
				print(thing.name + ' - '+ thing.description)
		self.check_exits()

	def locked(self, bool):
		return bool
	
	def unlock(self, items):
		if not(locked):
			print('location does not need to be unlocked')
		if locked and not(helicopter in items):
			print ('location is locked. You need flying transportation to get there safely.')
		if locked and helicopter in items:
			print('you get in helicopter')
			self.locked = False

	def take(self, thing):
		return self.things.pop(thing)

	def check_exits(self):
		print('You can exit to:')
		for exit in self.exits:
			print('   ', exit)

	def add_exits(self, places):
		for place in places:
			self.exits[place.name] = (place, place.description)