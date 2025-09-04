#Ask the user to enter a number under 20. If they enter a number that is 20 or more, display the message 'Too High'.
#Otherwise, display the message 'Thank you,;
#Adam Belkacemi
#4/9/2025

number = int(input('Enter a number below 20 '))

if (number<20):
    print("Thank you")
    
elif (number>20):
    print("Too high")
