dict1 = {1: 'Monday', 2: 'Tuesday', 3: "Wednesday", 4: "Thursday"}
# dict1 = {1: 'Monday', 2: 'Tuesday', 3: "Wednesday"}
rev_dict1 = {v : k for k, v in dict1.items()}

print(dict1[1])


print(rev_dict1)
dict1[5] = "Friday"

print(dict1)
