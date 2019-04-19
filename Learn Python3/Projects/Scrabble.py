import string
letters = zip(string.ascii_lowercase, string.ascii_uppercase)
#letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
player_to_points = {}



letter_to_points = { k:v for k,v in zip(letters, points) }
letter_to_points[''] = 0
def score_word(word):
	point_total = 0
	for i in word:
		for k,v in letter_to_points.items():
			if i in k:
				point_total += v
	return point_total

def play_word(player, word):
	if player in player_to_words:
		for k,v in player_to_words.items():
			if k == player and word not in v:
				v.append(word)

def update_point_totals():
	for player,words in player_to_words.items():
		player_points = 0
		for word in words:
			player_points += score_word(word)
		player_to_points[player] = player_points

brownie_points = score_word("BROWNIE")

play_word('player1', 'FUNNY')
play_word('Lexi Con', 'INSANE')
play_word('Lexi Con', 'BULLY')
play_word('wordNerd', 'yellow')


update_point_totals()
print(player_to_points)



#print(brownie_points)

