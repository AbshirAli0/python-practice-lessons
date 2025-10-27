# # comprehensions practice

# # list all even numbers 1-30
# evens = [n for n in range(1,31) if n % 2 == 0]
# print(evens)

# # list of squares from 1-10
# squared = [n**2 for n in range(1,11)]
# print(squared)

# # names starting with A
# names = ["Ali","John","Mike","Angela"]
# a_names = [n for n in names if n.startswith("A")]
# print(a_names)

# # nested and conditional lists comp

# # flatten 2d list
# data = [[1,2,3],[4,5],[6]]
# flat = [num for sublist in data for num in sublist]
# print(flat)

# # even and odd labels
# labels = ["Even" if n % 2 == 0 else "odd" for n in range(10)]
# print(labels)

# # xy pairs where x doesn't equal y
# pairs = [(x,y) for x in [1,2,3,4] for y in [1,2,3,4] if x != y]
# print(pairs)

# # Dictionary comprehensions - syntax
# # {key_expression: value_expression for item in iterable if condition}
# nums  = [1,2,3,4]
# squared_dict = {n: n**2 for n in nums if n % 2 == 0}
# print(squared_dict)

# # count word length
# sentence = "the quick brown fox jumps over the lazy dog"
# word_count = {word: len(word) for word in sentence.split()}
# print(word_count)

# # sets
# nums = [1,2,2,3,4,4]
# unique_squares = {n ** 2 for n in nums}
# print(unique_squares)

# # dict mapping 1-5 to cubes
# cubed = {n: n**3 for n in range(10)}
# print(cubed)

# # dict mapping words to uppercase
# words = ["apple", "banana", "cherry"]
# word_upper = {word: word.upper() for word in words}
# print(word_upper)

# # set of unique even numbers from a list with duplicates
# nums = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# unique_evens = {n for n in nums if n % 2 == 0}
# print(unique_evens)

# # reverse a dict
# original = {'a': 1, 'b': 2, 'c': 3}
# reversed_dict = {v:k for k, v in original.items()}
# print(reversed_dict)

# # flatten and filter even numbers from list of lists
# list = [[1, 2, 3], [4, 5], [6]]
# even_list = [num for group in list for num in group if num % 2 == 0]
# print(even_list)

# # filtering data from complex list structures
# people = [
#     {"name": "Abshir", "age": 22},
#     {"name": "Ali", "age": 30},
#     {"name": "Layla", "age": 19},
# ]
# adults = [p["name"] for p in people if p["age"] >= 21]
# print(adults)

# adult_dict = {p["name"]: p["age"] for p in people if p["age"] >= 21}
# print(adult_dict)

#assignment
#Part1 (listed Comprehension) - Create a list of all odd numbers between 1–30.

odd_numbers = [n for n in range(1,31) if n % 2 != 0]

print(odd_numbers)

# Create a list of squares of numbers from 1–10.

squared = [n**2 for n in range(1,11)]
print(squared)

# From the list ["Ali", "Layla", "Adam", "Zoe", "Abshir"], make a list of names starting with "A"

names = ["Ali", "Layla", "Adam", "Zoe", "Abshir"]

A_names = [n for n in names if n.startswith("A")]
print(A_names)

# Create a list of strings that say "even" or "odd" for each number in range(10).

even_odd_list = [ "Even" if n % 2 == 0 else "Odd"for n in range(10) ]

print(even_odd_list)

#part 2 (Nested Comprehension) - Given matrix = [[1, 2, 3], [4, 5], [6, 7]], flatten it into a single list.

matrix = [[1, 2, 3], [4, 5], [6, 7]]

flattened = [value for group in matrix for value in group]

print(flattened)

# From the same matrix, create a new list containing only even numbers.

matrix = [[1, 2, 3], [4, 5], [6, 7]]

even_matrix = [value for group in matrix for value in group if value % 2 == 0]

print(even_matrix)

# Generate all (x, y) pairs where x and y come from [1, 2, 3, 4] but x != y.

xy_pairs = [(x , y) for x in [1,2,3,4] for y in [1,2,3,4] if x != y]
print(xy_pairs)

# Create a mini multiplication table (1–3 × 1–3) as strings (like "2x3=6").

multiplication_table = [(f"{x} x {y} = {x*y}") for x in [1,2,3] for y in [1,2,3]]

print(multiplication_table)

#part 3 (dictionary Comprehensions) - Create a dictionary mapping numbers 1–5 to their cubes.

dic_numbers = {n: n**3  for n in range(1,6)}
print(dic_numbers)

# Given words = ["apple", "banana", "pear"], create a dictionary mapping each word to its uppercase form.

words = ["apple", "banana", "pear"]

upper_words = {word: word.upper() for word in words}

print(upper_words)

# From nums = [1, 2, 3, 4, 5, 6], make a dictionary of even squares only.

nums = [1, 2, 3, 4, 5, 6]

squared_nums = {n:n**2 for n in nums if n % 2 == 0}

print(squared_nums)

#Reverse this dictionary:

grades = {"Ali": 90, "Layla": 85, "Abshir": 95}

reversed = {v:k for k, v in grades.items()}

print(reversed)

# part4 - set Comprehensions - From nums = [1, 2, 2, 3, 4, 4, 5], create a set of unique squares.

nums = [1, 2, 2, 3, 4, 4, 5]

unique_squares  = {n**2 for n in nums}

print(unique_squares)

# From the same list, create a set of unique even numbers.

unique_even_nums  = {n for n in nums if n % 2 == 0}

print(unique_even_nums)

# create a set of all unique letters

sentence = "the quick brown fox jumps over the lazy dog"

unique_letters = {n for n in sentence if n != " " }

print(unique_letters)