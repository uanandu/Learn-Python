# Chapter 5: If statements
# 5-2: Conditional tests

print("True tests")
print("----------")

food = "Biriyani"
print("Is food == 'Biriyani' ? I predict True.")
print(food == 'Biriyani')

print("False tests")
print("-----------")
print("Is food == 'Aviyal' ? I predict False.")
print(food == 'Aviyal')

print("################")
# 5-3: Alien Colors #1
alien_color = "green"
if (alien_color == "green"):
	print("Player has earned 5 points!")
if (alien_color == "yellow"):
	print("You guessed wrong.")

# 5-4: Alien Colors #2
if (alien_color == "green"):
	print("Player has earrned 5 points")
else:
	print("Player has earned 10 points")

# 5-5: Alien Colors #3
if (alien_color == "green"):
	print("Player has earned 5 points")
elif (alien_color == "yellow"):
	print("Player has earned 10 points")
elif (alien_color == "red"):
	print("Player has earned 15 points")
else:
	print("Nothing to see here")

# 5-6: Stages of Life
input_age = input("What is your age?\n")
AGE = int(input_age)

if (AGE < 2):
	print("You are a baby!")
elif (AGE >= 2 and AGE < 4):
	print("You are a toddler!")
elif (AGE >= 4 and AGE < 13):
	print("You are a kid!")
elif (AGE >= 13 and AGE < 20):
	print("You are a teenager!")
elif (AGE >= 20 and AGE < 65):
	print("You are an adult!")
elif (AGE >= 65):
	print("You are an elder!")



# Favorite fruit

