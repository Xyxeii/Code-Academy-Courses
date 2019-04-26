class Menu():
	def __init__(self, name, items, start_time, end_time):
		self.name = name
		self.items = items
		self.start_time =start_time
		self.end_time = end_time

	def __repr__(self):
		return "The {name} menu is available from {start} to {end}.".format(name=self.name, start=self.start_time, end=self.end_time)

	def calculate_bill(self, purchased_items):
		price = 0.00
		for item in purchased_items:
			price += self.items[item]
		return '$' + str(price)

class Franchise():
	def __init__(self, address, menus):
		self.address = address
		self.menus = menus

	def __repr__(self):
		return self.address

	def available_menus(self, time):
		def convertTime(ctime):
			if ctime[-2:] == 'pm' and ctime[:-2] != '12':
				convTime = int(ctime[:-2]) + 12
			else:
				convTime = int(ctime[:-2])
			return convTime
		available_menus = []
		for i in range(len(self.menus)):
			name = self.menus[i].name
			startTime = convertTime(self.menus[i].start_time)
			endTime = convertTime(self.menus[i].end_time)
			if startTime <= convertTime(time) and endTime >= convertTime(time):
				available_menus.append(name)
		if available_menus:
			return ', '.join(available_menus)
		else:
			return 'There are no available menus at this time.'

class Business():
	def __init__(self, name, franchises):
		self.name = name
		self.franchises = franchises

	def __repr__(self):
		return self.franchises



brunch = Menu('Brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, '11am', '4pm')

early_bird = Menu('Early Bird Dinner', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, '3pm', '5pm')

dinner = Menu('Dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, '5pm', '11pm')

kids = Menu('Kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, '11am', '9pm')

arepas_menu = Menu('Take a\' Arepa', {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, '10am', '8pm')

#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
#print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Stree", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

basta_fazoolin = Business("Basta Fazoolin", [flagship_store, new_installment])
take_a_arepa = Business("Take a' Arepa", [arepas_place])

print(arepas_place.available_menus("9am"))