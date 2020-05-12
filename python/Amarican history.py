print("Fill out as if you were in the cold war era.")
print("Who are the Superpower country?")
country = input()
if country == "U.S":
	print("The other one")
	country = input()
	if country == "USSR":
		print("The thing that makes the Superpowers are the _______?")
		thing = input()
		if thing == "Nukes":
			print("What else?")
			thing = input()
			if thing == "Missile":
				print("Correct")
			else:
				print("Wrong")
		elif thing == "Missile":
			print("What else?")
			thing = input()
			if thing == "Nukes":
				print("Correct")
		else:
			print("Wrong")
	else:
		print("Wrong")
elif country == "USSR":
	print("The other one")
	country = input()
	if country == U.S:
		print("The thing that makes the Superpowers are the _______?")
		thing = input()
		if thing == "Nukes":
			print("What else?")
			thing = input()
			if thing == "Missile":
				print("Correct")
			else:
				print("Wrong")
		elif thing == "Missile":
			print("What else?")
			thing = input()
			if thing == "Nukes":
				print("Correct")
			else:
				print("Wrong")
		else:
			print("Wrong")
	else:
		print("Wrong")
else:
	print("Wrong")
input("press enter to exit")