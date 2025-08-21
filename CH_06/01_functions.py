# Function is a group of statements that perform specific tasks
# Repeat = Redundant

# a = 5
# b = 10
# sum = a + b
# print(sum)

def sum(a,b):
    return a+b

print(sum(1,8))


# average of 3 numbers

def average(a,b,c):
    result = (a + b + c)/3
    return result

print(average(5,7,9))


# Built-In Function

print("Hello World")
print(len("Chandrakant"))
print(range(1,10))


# User Defined Funtion

def cal_pro(a=1,b=1): # Default parameter if function does not have any arguments
    return a * b

print(cal_pro())


# 

cities = ["Delhi","Kolkata","Mumbai","Bengluru","Chennai","Hydrabad"]
heroes = ["SuperMan","IronMan","CaptainAmerica","ShaktiMan","BatMan"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)
print()
print_list(heroes)
print()



# Write a program to find the factorial of n.

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(5)



# Write a program to convert USD to INR

def curr_conv(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")

curr_conv(1000)



# write a program to know if the number is odd or even

def fun(n):
    if(n%2 == 0):
        print("Even")
    else:
        print("Odd")
    
fun(151)

