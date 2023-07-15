# Lists

# 3-1: Names
names = ["Eric", "Barney", "Ross", "Rachel"]
for name in names:
    print(name)

print("####################################")
# 3-2: Greetings

# Using match
print("First method:")
for name in names:
    match name:
        case "Eric":
            print("Hi Eric, Whatup?!")
        case "Barney":
            print("Comment t'allez vous, Barney?")
        case "Ross":
            print("Are you fiiiiineee, Ross??")
        case "Rachel":
            print("What is in your bag????")

        case _:
            print("stupid answer!!")

print("#####################################")
print("Second method: ")

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