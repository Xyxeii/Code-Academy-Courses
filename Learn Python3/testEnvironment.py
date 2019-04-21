names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
def count_first_letter(names):
	new_dict = { k[0]:0 for k,v in names.items() }
	for k,v in names.items():
		new_dict[k[0]] += len(v)
	return new_dict

print(count_first_letter(names))
