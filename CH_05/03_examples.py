# for loop with a list Concept: Iterating over a known sequence of items.
# Printing each item in a shopping list.

fruits = ["Apple","Banana","Mango","Orange","Papaya"]

for fruit in fruits:
    print(f"I want to bug {fruit}")




# while loop - Concept: Repeating a block of code while a condition is true. You must manage the loop variable yourself.
# Counting down to a rocket launch.

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast Off")




# range() - Concept: Executing a loop a specific number of times.
# Printing the first 5 multiples of 3.

n = 3
for i in range(1,6):
    result = i * n
    print(f"3 X {i} = {result}")
    



# Loop with break statement Concept: Exiting a loop prematurely when a specific condition is met.
# Searching for a number in a list and stopping once you find it.

numbers = [14, 27, 33, 48, 52, 61]
x = 52

for num in numbers:
    print(f"Checking {num}")
    if(num == x):
        print(f"Found it {x}. It is in the list")
        break




# Loop with continue statement Concept: Skipping the rest of the current iteration and moving to the next one.
# Printing only the odd numbers from a list.

for i in range(1,11):
    if(i % 2 == 0):
        continue
    print(i)
    



# Nested Loops -> Concept: Placing one loop inside another.
# Generating a simple multiplication table.

for i in range(1,4):  # Outer loop for the first number
    for j in range(1,4): # Inner loop for the second number
        product = i * j
        print(f"{i} x {j} = {product}", end=" | ")  # 'end' changes the default newline
    print() # Print a newline after each inner loop finishes




# Loop with else clause Concept - The else block runs only if the loop completed normally (i.e., not stopped by a break).
# Checking if a number is prime.

num  = 11
for divisor in range(2,num):
    if(num % divisor == 0):
        print(f"{num} is not prime. Divisible by {divisor}")
        break
else:  # This belongs to the FOR loop, not the IF statement!
    print(f"{num} is a prime number")




# Using enumerate() Concept: Getting both the index and the value of each item in a sequence during iteration.
# Displaying a ranked list of items.

programming_langs = ["Python", "JavaScript", "Java", "C++"]

for index, lang in enumerate(programming_langs, start=1): # start=1 begins indexing at 1
    print(f"{index} : {lang}")




# Using zip() Concept: Iterating over two or more sequences in parallel.
# Combining data from two different lists.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names,scores):
    print(f"{name} scored {score}")




# Dictionary Iteration with .items() Concept: Efficiently looping through both the keys and values of a dictionary.
# Processing configuration settings or any key-value data.

ser_profile = {
    "username": "data_ninja",
    "email": "ninja@example.com",
    "level": "admin"
}

print("User profile details")
for key, value in ser_profile.items():
    print(f"{key.title()}:{value}")