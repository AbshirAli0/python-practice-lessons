# profile = {
#     "name": "Abshir",
#     "age": 23,
#     "language": "english",
#     "hobbies": "Exercising"
# }

# #print(profile["name"])

# user = {}

# # to add key value pairs
# user["username"] = "abshir1001"
# user["email"] = "myemail@fakenews.com"

# #print(user)

# # to edit
# user["email"] = "deeznuts@gmail.com"

# #print(user)

# # to remove
# del user["email"]

# #print(user)

# #.get() - used to access values safely without facing errors if key doesn't exist
# #print(user.get("email"))
# #print(user.get("username"))

# # iterating through a dictionary

# for key in profile:
#     print(key, profile[key])

# for key, value in profile.items():
#     print(f"{key}:{value}")

# print(profile.keys())
# print(profile.values())

# #book1

# book1 = {
#     "title": "Harry Potter",
#     "author": "J.K Rowling",
#     "year": "2002"
# }

# for key in book1:
#     print("This is the key: ", key)

# for value in book1.values():
#     print("this is the value: ", value)

# for key, value in book1.items():
#     print(f"{key}: {value}")

# print(book1)

# book1["author"] = "Dr.Seuss"

# print(book1)

# del book1["year"]

# print(book1)

# #counting occurences

# words = ["apple", "banana", "grapes", "orange"]

# counts = {}

# for w in words:
#     counts[w] = counts.get(w,0) + 1
# print(counts)

# #sets = a set of unique elements that are unordered and mutable

#HOMEWORK
#Part 1 Dictionary
#1
student = {
    "name": "Abshir",
    "age": 23,
    "courses": ["Math", "History"]
}

print(student)

student["major"] = "Political Science"

print(student)

student["age"] = 24

print(student)

del student["courses"]

print(student)

for k , v in student.items():
    print(f"{k}: {v}")

#2
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for word in words:
    count[word] = count.get(word,0) + 1

print(count)    

# a list is an ordered collection of items, while a dictionary stores key-value pairs. a dictionary is preferred when you want to associate values with a unique key for fast access.