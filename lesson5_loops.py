fruits = ["apple", "banana", "cherry"]

# for loop
for fruit in fruits:
    print(fruit)


for i in range(3):
   print(i)

# while loop

count = 0

while count < 5:
    print(count)
    count += 1

# break
for i in range(10):
    if i == 5:
        break
    print("break", i)

# continue

for i in range(5):
    if i == 2:
        continue
    print(i)

# loop else clause

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("loop finished")

#homework

1.
for i in range(1, 11):
    print("question 1", i)


2.

count = 10

while count >= 0:
    print("question 2:", count)
    count -= 2

3. 

for i in range(1,10):
    if i == 7:
        break
    print(i)

4.

for i in range(1,5):
    if i == 3:
        continue
    print(i)

5.

for i in range(1,5):
    if i % 6 == 0:
        break
else:
    print("no divisible by 6 found")