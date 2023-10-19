# 3. Display numbers from -10 to -1 using for loop

for num in range(-10, 0):
    print(num)

#4. Calculate the cube of all numbers from 1 to a given number from user

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    cube = i * i * i
    print(f"The cube of {i} is: {cube}")