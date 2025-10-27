#mini exercise

1. 
movies = ["Shrek", "Cars", "Charlie in the cholcate factory", "TMNT", "Suicide Squad"]

print(movies[0], movies[-1] )

2.

movies.append("Matilda")
print(movies)

3.

#number = (1,2,3,4)

#number.append(5)
# AttributeError: 'tuple' object has no attribute 'append'

4.

for i in movies:
    print(i)

for i in range(len(movies)):
    print(i, movies[i])

5.

matrix = [
    [1,2],
    [3,4]
]

bottom_element = matrix[1][1]

print(bottom_element)