# Working with lists

# 4-1: Pizzas
pizzas = ["All-dressed", "Chicken-pesto", "Boston", "Alfredo-chicken"]

for pizza in pizzas:
	print(f"I love {pizza} pizza!")

print("I really love pizza!!!!")

# 4-2:Animals

animals= ["cat", "dog", "goat", "chicken", "hamster"]

for animal in animals:
	print(f"A {animal} is a great pet")

print("All these animals have legs in common")

# 4-3: Counting to twenty
print("Counting to twenty....")
for number in range(1,21):
	print(number)
print("----------------------")

# 4-4: One million
#print("Counting to one million...")
#for  number in range(1000000):
#	print(number)


# 4-5: summing a million
#print("summing a million....")
#million_number_list=[]
#for number in range(1, 10000001):
#	million_number_list.append(number)

#print(f"The sum is {sum(million_number_list)}")

# 4-6: Odd numbers
number_list= []
for number in range(20):
	 number_list.append(number)

odd_numbers = []
for number in number_list:
	if(number % 2 != 0):
		odd_numbers.append(number)

print(odd_numbers)

# 4-7: Threes
number_list_to_thirty = []
for number in range(3,31):
	number_list_to_thirty.append(number)

success_numbers_three= []
for number in number_list_to_thirty:
	if(number % 3 == 0):
		success_numbers_three.append(number)

print(success_numbers_three)

# 4-8: Cubes
# 4-9: Cube comprehension
cubes_list = []
for number in range(1,11):
	my_cube = number**3
	print(my_cube)
	cubes_list.append(my_cube)

print(cubes_list)

# 4-10: Slices
# Here we targer success_numbers_three list

print(f"The first three items in the list are: {success_numbers_three[:3]}")
print(f"Three items frmo the middle of the list are:{success_numbers_three[3:6]}")
print(f"The last three items in the list are:{success_numbers_three[-3:]}")

# 4-11: My pizzas, Your pizzas

friend_pizzas = pizzas[:]

pizzas.append("BBQ")
friend_pizzas.append("Veggie")

print("My favorite Pizzas are: ")
for pizza in pizzas:
	print(f"{pizza}")

print("My friend's favorite Pizzas are: ")
for pizza in friend_pizzas:
	print(f"{pizza}")

