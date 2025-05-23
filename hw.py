try:
    x = int(input("Enter your age: "))
except:
    print("Enter your age!!")

if x%2 == 0:
    print ("Your age is even")
else:
    print ("Your age is odd")