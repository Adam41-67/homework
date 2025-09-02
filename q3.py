height = int(input("Whats your height in centimetres? "))
feet = (height/2.54)
inches = (feet/12)
inches1 = feet % 12
feet = int(feet)
inches = int(inches)
inches1 = int(inches1)
print (inches,"feet",inches1,"inches")