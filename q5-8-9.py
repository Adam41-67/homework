#print a multiplication table of each number
#Adam Belkacemi
#11/9/2025

number = int(input("Enter a number "))
for iteration in range(1,13):
    print(number,"x",iteration,"=",number*iteration)