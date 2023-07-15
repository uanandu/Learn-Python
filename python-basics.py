# 2-1 -> Simple message
message = "YOU CAN'T HANDLE THE TRUTH!!!"
print(message)
print("##################################################")

# 2-2 -> Simple messages
message_one = "Are you the one?!"
print(message_one)

message_one = "Yes, master!! I am!"
print(message_one)
print("##################################################")

# 2-3 -> Personal message
person1 = "Matthias"
print(f"Hi {person1}, would you like to learn some python today?!")
print("##################################################")

# 2-4 -> Name cases
person2 = "Quill"
print(f"here is the lowercase: {person2.lower()}")
print(f"here is the uppercase: {person2.upper()}")
print(f"here is the titlecase: {person2.title()}")
print("##################################################")

# 2-5: Famous quote
print("here is my favorite quote:")
print("\"Give me freedom or give me death\"")
print("##################################################")

# 2-6: Famous quote 2:
famous_person1 = "Albert einstein"
famous_quote1 = "\"A person who never made a mistake never tried anything new\""
print(f"here is a famous quote from {famous_person1}: \n{famous_quote1}")
print("##################################################")

# 2-7: Stripping names
# here we use lstrip(), rstrip() and strip()
name1 = " \n\tModel:iSteady XE\n\tType: Gimbal\n\tUse: Photo   "
name1_left = name1.lstrip()
name1_right = name1.rstrip()
name1_all = name1.strip()

print(name1_left)
print(name1_right) 
print(name1_all)

# 2-8 File extensions
# here we use removeprefix() and removesuffix()
filename = "python_notes.txt"
removed_suffix = filename.removesuffix(".txt")
print(f"Here is the file without extension: {removed_suffix}")

