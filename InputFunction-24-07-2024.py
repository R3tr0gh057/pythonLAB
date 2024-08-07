# Print format function

temp = input("What is your name? \n")
print(f"hello {temp}")

# Integer function

age = input("Enter your age? \n")
age = int(age)
print(f"you are {age} years old")

# Inline input function

print("hello "+input("name? \n"))

# Swap data without temp

a = 12
b = 10

print(f"a : {a} b: {b}")

a , b = b , a

print(f"a : {a} b : {b}")

# Max Min without condition

c = 12
d = 6

print("max = ",((c+d)+abs(c-d))/2)
print("min = ",((c-d)+abs(c-d))/2)