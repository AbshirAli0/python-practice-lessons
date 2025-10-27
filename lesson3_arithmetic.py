x = 10
y = 3

#1 

'''
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)


'''

print("arithmetic")

for op, result in [("x + y", x +y), ("x - y", x - y), ("x * y", x * y), 
                   ("x / y", x / y), ("x % y", x % y), ("x ** y", x ** y)]:
    print(op, "=", result)
#2'




print (x == y)
print(x > y)
print(x < y )
print(x != y)
print(x >= y)
print( x <= y)

#3

is_sunny = True
have_umbrella = False

print(is_sunny and have_umbrella)
print(is_sunny or have_umbrella)
print( not is_sunny)

#4
score = 50

score += 2
print(score)
score -= 25
print(score)
score *= 50
print(score)
score /= 2
print(score)

