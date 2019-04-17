def groundShipping(weight):
	cost = ""
	flatCharge = 20.00
	if weight > 10:
		cost = weight * 4.75
	elif (weight > 6 and weight <= 10):
		cost = weight * 4.00
	elif (weight > 2 and weight <= 6):
		cost = weight * 3.00
	elif weight < 2:
		cost = weight * 1.50
	return cost + flatCharge

def droneShipping(weight):
	cost = ""
	flatCharge = 0.00
	if weight > 10:
		cost = weight * 14.25
	elif (weight > 6 and weight <= 10):
		cost = weight * 12.00
	elif (weight > 2 and weight <= 6):
		cost = weight * 9.00
	elif weight < 2:
		cost = weight * 4.50
	return cost + flatCharge


def cheapestShipping(weight):
	name = ""
	ground = groundShipping(weight)
	drone = droneShipping(weight)
	premium = 125.00
	lowestPrice = min(ground, drone, premium)
	if lowestPrice == ground:
		name = "Ground"
	elif lowestPrice == drone:
		name = "Drone"
	else:
		name = "Premium"
	return "{name} Shipping is your cheapest option! Price: ${lowestPrice}".format(lowestPrice = lowestPrice, name = name)

print(cheapestShipping(4.8))
print(cheapestShipping(41.5))


##Working Code

# def groundShipping(weight):
# 	cost = ""
# 	flatCharge = 20.00
# 	if weight > 10:
# 		cost = weight * 4.75
# 	elif (weight > 6 and weight <= 10):
# 		cost = weight * 4.00
# 	elif (weight > 2 and weight <= 6):
# 		cost = weight * 3.00
# 	elif weight < 2:
# 		cost = weight * 1.50
# 	return cost + flatCharge

# def droneShipping(weight):
# 	cost = ""
# 	flatCharge = 0.00
# 	if weight > 10:
# 		cost = weight * 14.25
# 	elif (weight > 6 and weight <= 10):
# 		cost = weight * 12.00
# 	elif (weight > 2 and weight <= 6):
# 		cost = weight * 9.00
# 	elif weight < 2:
# 		cost = weight * 4.50
# 	return cost + flatCharge


# def cheapestShipping(weight):
# 	ground = groundShipping(weight)
# 	drone = droneShipping(weight)
# 	premium = 125.00
# 	if (ground < drone) and (ground < premium):
# 		return "Ground Shipping is your cheapest option! Price: $" + str(ground)
# 	elif (drone < ground) and (drone < premium):
# 		return "Drone Shipping is your cheapest option! Price: $" + str(drone)
# 	else:
# 		return "Premium Shipping is your cheapest option! Price: $" + str(premium)

# print(cheapestShipping(4.8))
# print(cheapestShipping(41.5))
