# # highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# # highlighted_poems_list = highlighted_poems.split(',')


# # highlighted_poems_stripped = [ i.strip() for i in highlighted_poems_list ]
# # highlighted_poems_details = [ i.split(':') for i in highlighted_poems_stripped ]
# # #print(highlighted_poems_details)

# # titles = [ i[0] for i in highlighted_poems_details]
# # poets = [ i[1] for i in highlighted_poems_details]
# # dates = [ i[2] for i in highlighted_poems_details]

# # for i in range(len(highlighted_poems_details)):
# #   print("The poem {TITLE} was published by {POET} in {DATE}.".format(TITLE = titles[i], POET = poets[i], DATE = dates[i]))


# # def fizzBuzz(multiple_of_3, multiple_of_5):
# # 	for i in range(1, 100):
# # 		if (i / multiple_of_3 == int(i / multiple_of_3)) and (i / multiple_of_5 == int(i / multiple_of_5)):
# # 			print("FizzBuzz")
# # 		elif i / multiple_of_3 == int(i / multiple_of_3):
# # 			print("Fizz")
# # 		elif (i / multiple_of_5 == int(i / multiple_of_5)):
# # 			print("Buzz")
# # 		else:
# # 			print(i)

# # def fizzBuzz(multiple_of_3, multiple_of_5):
# # 	for i in range(1, 100):
# # 		if i % 3 == 0 and i % 5 == 0:
# # 			print("FizzBuzz")
# # 		elif i % 3 == 0:
# # 			print("Fizz")
# # 		elif i % 5 == 0:
# # 			print("Buzz")
# # 		else:
# # 			print(i)

# #fizzBuzz(3, 5)

# # def count_multi_char_x(word, x):
# # 	count = 0 
# # 	for i in range(len(word)):
# # 		if word[i:i+len(x)] == x:
# # 			count += 1
# # 	return count

# # def reverse_string(word):
# # 	reverse = ""
# # 	for i in range(len(word)):
# # 		reverse += word[(len(word) - 1) - i]
# # 	return reverse

# # print(reverse_string("Hello world!"))

# # def add_exclamation(word):
# # 	yay = word
# # 	if len(word) < 20:
# # 		while len(yay) < 20:
# # 			yay += "!"
# # 		return yay
# # 	else:
# # 		return word
# # print(add_exclamation("Codecademy is the best place to learn"))

# # daily_sales = \
# # """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
# # 09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
# # white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
# # ;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
# # ;,;   $5.13   ;,; white   ;,; 09/15/17,
# # Eduardo George   ;,;$20.39;,; white&yellow 
# # ;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
# # purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
# # purple&yellow ;,;09/15/17,   Shaun Brock;,; 
# # $17.98;,;purple&yellow ;,; 09/15/17 , 
# # Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
# # Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
# # Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
# # 09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
# # white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
# # ;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
# # $8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
# # 09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
# # green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
# # ;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
# # Israel Cummings;,;   $11.86   ;,;black;,;  
# # 09/15/17,   June Doyle   ;,;   $22.29 ;,;  
# # black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
# # $8.35;,;   white&black&yellow   ;,;   09/15/17,   
# # Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
# # ;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
# # ;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
# # ;,; 09/15/17   ,Hubert Miles;,;   $3.59   
# # ;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
# # ;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
# # black   ;,;   09/15/17 , Audrey Ferguson ;,; 
# # $5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
# # $17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
# # Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
# # 09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
# # yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
# # yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
# # ;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
# # $14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
# # ;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
# # black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
# # ;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
# # $8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
# # ;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
# # ,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
# # 09/15/17 , Melody Moran ;,;   $30.84   
# # ;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
# # $12.31 ;,; green&yellow&black;,;   09/15/17 ,
# # Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
# # ,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
# # 09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
# # white&yellow&black ;,;09/15/17   ,   Dale Brady   
# # ;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
# # Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
# # ,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
# # 09/15/17, Angelica Garza;,;$11.60;,;white&black   
# # ;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
# # white&black&red ;,;09/15/17   ,   Rex Hudson   
# # ;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
# # ;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
# # Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
# # ;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
# # green&purple&yellow ;,;09/15/17   ,Stanley Holland 
# # ;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
# # Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
# # ;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
# # red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
# # green&red ;,;   09/15/17   ,Irving Patterson 
# # ;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
# # Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
# # Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
# # Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
# # ,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
# # Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
# # , Beatrice Newman ;,;$22.45   ;,;white&purple&red 
# # ;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
# # red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
# # black&red;,; 09/15/17,   Javier Bailey   ;,;   
# # $24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
# # Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
# # ,   Traci Craig ;,;$0.65;,; green&yellow;,; 
# # 09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
# # green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
# # ;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
# # ;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
# # Leonard Guerrero ;,;   $1.86   ;,;yellow  
# # ;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
# # 09/15/17   ,Donna Ball ;,; $28.10  ;,; 
# # yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
# # $9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
# # $16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
# # ;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
# # Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
# # ;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
# # green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
# # green&yellow;,;09/15/17,Malcolm Morales ;,;   
# # $24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
# # Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
# # ,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
# # , Leticia Manning;,;$15.70 ;,; green&purple;,; 
# # 09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
# # 09/15/17,Lewis Glover;,;   $13.66   ;,;   
# # green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
# # ;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
# # ;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

# # daily_sales_replaced = daily_sales.split(";,;")
# # print(daily_sales_replaced)


# # biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

# # for company in biggest_brands:
# #   print(company + " has a value of " + str(biggest_brands[company]) + " billion dollars. ")

# # for company, value in biggest_brands.items():
# #   print(company + " has a value of " + str(value) + " billion dollars. ")

# # class NoCustomAttributes:
# #   pass

# # attributeless = NoCustomAttributes()

# # getattr(attributeless, 'fake_attribute', "doesn't exists")

# # def find_mission(array, arraymissing):
# # 	new_list = []
# # 	for i in range(len(array)):
# # 		if array[i] in arraymissing:
			

# def reverse(x):
# 	return x[::-1]

# print(reverse("olleH"))

# def full_name(fs, ps):
# 	return sum(fs) - sum(ps)

# print(full_name([2, 3, 4, 5, 6],[2, 3, 4, 6]))
names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
def count_first_letter(names):
	new_dict = { k[0]:0 for k,v in names.items() }
	for k,v in names.items():
		new_dict[k[0]] += len(v)
	return new_dict

print(count_first_letter(names))