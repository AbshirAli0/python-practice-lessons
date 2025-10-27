age = 15

# if/else statement
if age >= 18:
    print("you are an adult")
else:
    print("you are a minor")


score = 75

#elif multiple conditions

if score >= 90:
    print("You got an A+")
elif score >=75:
    print("you got a B")
elif score >=60:
    print("mate you got a C")
else:
    print("you Failed Mate")

age = 17
has_ticket = True

# nested if statement
if age >= 18:
    if has_ticket:
        print("you can enter the concert")
    else:
        print("you need a ticket")
else:
    print("you are too young")

if age >=18 and has_ticket:
    print("Entry allowed")
else:
    print("fuck off!")

# homework

1. 
temp = 21

if temp > 30:
    print("HOT")
elif 20 <= temp <= 30:
    print("warm")
else:
    print("cold")

2.

age = 23

if age < 13:
    print("child")
elif 13 <= age < 18:
    print("Teen")
else:
    print("Adult")


3.

username = "AbshirAli"
password = "deezNuts"

if username == "admin" and password == "1234":
    print("access granted")
else:
    print("access denied")

4.

has_ticket = True
age = 16

if age >= 18:
    if has_ticket:
        print("Allowed")
    else:
        print("you need a ticket") 
else:
    print("NO ticket")