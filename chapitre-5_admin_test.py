# 5-8: Hello admin

my_usernames = ["Anandu", "Andrea", "Anne", "Alicia", "Sam", "admin"]

for user in my_usernames:
	if (user == "admin"):
		print(f"Hello {user}, would you like a status report?!")
	else:
		print(f"Hello {user}, thanks for logging in again!")

# 5-9: No users
empty_usernames_list = []
if empty_usernames_list:
	print("Good, we got users!")
else:
	print("We need to find some users!")

# 5-10: Checking username
current_users = ["Arjun", "Sara", "Kuttan", "Anandu", "Andrea"]
new_users = ["Anne", "Marie", "Anandu", "Sara", "Sari"]


for  user in new_users:
	for user_check in current_users:
		if (user == user_check):
			print(f"{user} isnt available!")
		else:	
			print(f"{user} is available!")


# 5-11: Ordinal numbers


