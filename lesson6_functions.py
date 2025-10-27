#define a function

def greet():
    print("Hello!")

greet()

#function Parameters
def greet_user(name):
    print(f"Hello, {name}")

greet_user("Abshir")
greet_user("Ali")

#Return Values
def add(a,b):
    return a + b

result = add(5,3)
print(result)

#Scope

x = 100 # global

def test_scope():
    x = 50 # local
    print("Inside function: ", x)

test_scope()
print("Outside funciton: ", x)

#default parameters

def greet(name = "friend"):
    print(f"hello, {name}")

greet()
greet("Abshir")

#Multiple Return Values

def get_user_info():
    name = "Abshir" 
    age = 22
    return name, age

n, a = get_user_info()
print(n,a)

#homework

1.

def square(num):
    return num ** 2

print(square(2))

2.

def greet_user(name,age):
    print(f"Hello {name}, you are {age} years old")

greet_user("Abshir", 23)

3.

def is_even(n):
    return n % 2 == 0
   
print(is_even(2))
print(is_even(3))



4.

def max_of_three(a,b,c):
 return max(a,b,c)

print(max_of_three(1,2,3))

5.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(3))

6.

x = 100

def number():
    x = 50
    return x

print(x)
print(number())