##Abruptly Goblins Planner

gamers = []

def add_gamer(gamer, gamers_list):
	try:
		if gamer['name'] and gamer['availability']:
			gamers_list.append( { k:v for k,v in gamer.items() } )
			print("{name} has been added to the list!".format(name = gamer['name']))
	except KeyError as e:
		print("{} doesn't exist".format(e))

def build_daily_frequency_table():
	weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
	return {k:0 for k in weekDays}

def calculate_availability(gamers_list, available_frequency):
	for gamer in gamers_list:
		for day in gamer['availability']:
			available_frequency[day] += 1

def find_best_night(availability_table):
	best_night = max(availability_table.values())
	for k in availability_table.keys():
		if availability_table[k] == best_night:
			return k

def available_on_night(gamers_list, day):
	available_gamers = []
	for gamer in gamers_list:
		if day in gamer['availability']:
			available_gamers.append(gamer['name'])
	return available_gamers

def not_available_on_night(gamers_list, day):
	not_available_gamers = []
	for gamer in gamers_list:
		if day not in gamer['availability']:
			not_available_gamers.append(gamer)
	return not_available_gamers


def send_email(gamers_who_can_attend, day, game):
	for gamer in gamers_who_can_attend:
		print(form_email.format(name = gamer, day_of_week = day, game = game))



##Adding gamers and availablility to the list
add_gamer({'name':'Kimberly Warner','availability': ["Monday", "Tuesday", "Friday"]}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

##Storing weekly table as a variable
count_availability = build_daily_frequency_table()

##Calculate number of people that can make it each day
calculate_availability(gamers, count_availability)

##Find the best night to host game night
game_night = find_best_night(count_availability)

##Create a list of people who can attend
attending_game_night = available_on_night(gamers, game_night)

##Create a form email to send out to players who can make it
form_email = 'Dear {name}, \nYou\'re invited to player {game} on {day_of_week} night!\nSee you then!\n'

##Send the email to everyone who can attend game night
send_email(attending_game_night, game_night, 'Abruptly Goblins!')

##Create a list of people who couldn't attend
unable_to_attend_best_night = not_available_on_night(gamers, game_night)

##Store a second weekly table as a variable
second_night_availability = build_daily_frequency_table()

##Calculate the number of people that can make the second night
calculate_availability(unable_to_attend_best_night, second_night_availability)

##Find the second best night to host another game night
second_night = find_best_night(second_night_availability)

##Create a list of people that can make the second night
available_second_game_night = available_on_night(gamers, second_night)

#Send the email to everyone who can attend the second night
send_email(available_second_game_night, second_night, 'Abruptly Goblins!')

