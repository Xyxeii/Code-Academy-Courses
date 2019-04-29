from money import Money
from datetime import date, datetime, timedelta
import operator

#print(date.today())
client_database = {}

class Art():
	def __init__(self, artist, title, medium, year, owner):
		self.artist = artist
		self.title = title
		self.medium = medium
		self.year = year
		self.owner = owner

	def __repr__(self):
		return '{name}. "{title}". {year}, {medium}. {ownername}, {ownerlocation}.'.format(
			name=self.artist,
			title=self.title,
			year=self.year,
			medium=self.medium,
			ownername=self.owner.name,
			ownerlocation=self.owner.location
			)


class Marketplace():
	def __init__(self, listings=None):
		self.listings = listings
		if self.listings == None:
			self.listings = {}

	def add_listing(self, name, price, start_date, expiry_date, seller):
		self.listings[name] = {'Price':price, 'List Date': start_date, 'Expires': expiry_date, 'Seller':seller}

	def remove_listing(self, listing):
		if listing in self.listings:
			del self.listings[listing]

	def show_listings(self):
		return self.listings


class Client():
	def __init__(self, name, wallet=0, location='Private Collection', is_museum=False):
		self.name = name
		self.wallet = wallet
		self.location = location
		self.is_museum = is_museum
		client_database[self.name] =  {'Location': self.location, 'is museum': self.is_museum, 'Wishlist': [], 'Account Balance': self.wallet}

	def buy_artwork(self, artwork):
		if self.name != artwork.owner.name:
			if artwork.title in veneer.listings:
				artwork.owner = self
				client_database[self.name]['Account Balance'] -= veneer.listings[artwork.title]['Price']
				client_database[veneer.listings[artwork.title]['Seller']]['Account Balance'] += veneer.listings[artwork.title]['Price']
				veneer.remove_listing(artwork.title)

	def sell_artwork(self, artwork, price, expires_in, start_time=date.today()):
		expiry_date = datetime.strftime(start_time + timedelta(days=expires_in), '%b %d, %Y')
		start_date = datetime.strftime(start_time, '%b %d, %Y')
		if artwork.owner.name == self.name:
			veneer.add_listing(artwork.title, price, start_date, expiry_date, artwork.owner.name)

	def account_balance(self, currency='USD'):
		return str(Money(client_database[self.name]['Account Balance'], currency))

	def add_wishlist(self, artwork):
		client_database[self.name]['Wishlist'].append(artwork.title)
		print("Added '{art}' to your wishlist! Type "".wishlist to view it!".format(art=artwork.title))

	def remove_wishlist(self, artwork):
		client_database[self.name]['Wishlist'].pop(client_database[self.name]['Wishlist'].index(artwork.title))
		print("Removed {art} from your wishlist.".format(art=artwork.title))

	def wishlist(self):
		return client_database[self.name]['Wishlist']




veneer = Marketplace()
edytta = Client('Edytta Halpirt')
moma = Client('The MOMA', 10000000, 'New York', True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)
#test_painting = Art("Martiniano, Anthony", "Boy with stuff", "paper", "2019", moma)


edytta.sell_artwork(girl_with_mandolin, 6000000, 30)
#moma.sell_artwork(test_painting, '$100M (USD)')

#moma.buy_artwork(girl_with_mandolin)

#print(moma.wallet)
#moma.add_wishlist(girl_with_mandolin)

#print(moma.wishlist())

#moma.remove_wishlist(girl_with_mandolin)
print("Listings:")
print(veneer.show_listings())

# print("\nDatabase:")
# print(client_database)

#print(moma.account_balance())

