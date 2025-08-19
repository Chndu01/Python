# Loops in Python
# Loops are used to repeat instructions.

# While loop

count = 1  # Iterator
while count <= 10:
    print("Hello",count)
    count += 1

print(count)



i = 1
while i<=5:
    print(i)
    i += 1

print(i)



i1 = 1
while i1 <= 100:
    print(i1)
    i1 += 1



i2 = 100
while i2 >= 1:
    i2 -= 1
    print(i2)



n = 3
i = 1
while i <= 10:
    print(n*i)
    i += 1



list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(list1):
    print(list1[idx])
    idx += 1


# Break and Continue


tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 91, 100)
x = 36
i = 0
while i < len(tup1):
    if(tup1[i] == x):
        print(f"found at index {i}")
        break
    else:
        print("Finding...")
    i += 1



i = 1
while 1 <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("End of Loop")



i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1





























