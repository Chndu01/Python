# for loop
# used for sequential traversal. for traversing list, string, tuples etc

list = [1, 2, 3, 4]

for nums in list:
    print(nums)



tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for num in tup:
    print(num)



str = "Chandrakant"

for char in str:
    print(char)
else:
    print("End")



nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in nums:
    print(num)



tupl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0

for el in tupl:
    if(el == x):
        print("Number found at ",idx)
    idx += 1


# range()
# range functions returns a sequence of numbers, string from 0 by default, and increaments by 1 (by default), and stops before a specified number.


seq = range(5)
for i in seq:
    print(i)


for i in range(10):
    print(i)


for i in range(1,50,5):
    print(i)


for i in range(1,101):
    print(i)


for i in range(100,0,-1):
    print(i)


n = int(input("Enter a Number : "))
for i in range(1,11):
    print(n*i)


# pass statement is null statement that does nothing. it is used as a placeholder for future code.


for i in range(5):
    pass

print("Some Useful Work")



n = 5
sum = 0
for i in range(1,n+1):
    sum += i

print("Total sum = ",sum)



