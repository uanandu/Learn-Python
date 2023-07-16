
# Lists

# 3-1: Names
names = ["Eric", "Barney", "Ross", "Rachel"]
for name in names:
    print(name)

print("####################################")
# 3-2: Greetings

# Using match
#print("First method:")
#for name in names:
#    match name:
#        case "Eric":
#            print("Hi Eric, Whatup?!")
##        case "Barney":
#            print("Comment t'allez vous, Barney?")
#        case "Ross":
#            print("Are you fiiiiineee, Ross??")
#        case "Rachel":
#            print("What is in your bag????")
#
#        case _:
#            print("stupid answer!!")
#
#print("#####################################")
#print("Second method: ")

# Using switch
def switch(name):
    if name == "Eric":
        return "Hi Eric, Whatup?!"
    elif name == "Barney":
        return "Comment t'allez vous, Barney?"
    elif name == "Ross":
        return "Are you fiiiiineee, Ross??"
    elif name == "Rachel":
        return "What is in your bag????"

for name in names:
    print(switch(name))

print("####################################")

# 3-3: Your Own list
mode_of_transportation = ["car", "Harley", "Bicycle"]

for item in mode_of_transportation:
    print(f"I would like to own a {item}!")

# 3-4 : Guest list
message = "We cordially invite you to  our function on 27th August 2023:"
guest_list = ["Asoka", "Chola", "Buddha", "Krishna", "Ram", "Jesus", "Anandu", "Athul"]
for guest in guest_list:
	print(message, f"{guest}")

# 3-5: Changing the guest list
print("After getting the RVSP response we see that some of the guests aren't gonna make it")
guest_list.remove("Asoka")
guest_list.insert(6, "Darwin")
for guest in guest_list:
	print(message, f"{guest}")

print("#################")
print("Two days later!!")
print("#################")

print("Hey guys,i've found a bigger table for you guys. I would love to transfer you to that and add some more members!!!!")

guest_list.insert(0, "Jaby")
guest_list.insert(5, "Anne")
guest_list.append("Andrea")

for guest in guest_list:
	print(f"Hey {guest}, please do show up at the place given in the invitation")

print("##########################")
print("The day before the wedding")
print("##########################")

for guest in guest_list:
	index_of_list = guest_list.index(guest)
	while(index_of_list <= 2):
		guest_list.pop(index_of_list)
		print(f"We deeply apologize for this last minute change, Unfortunately we don't be able to accomodate you {guest}. \n Please accept this gift that we are sending out to you!. \n Thanks")

for guest in guest_list:
	print(f"Hey {guest}, you are still invited and your seat is reserved for the ceremony.\n We would be esctatic to see you enjoy the wedding")


