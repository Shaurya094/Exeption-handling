try:
    x = int(input("Enter a number: "))
    print ("The number entered was: ", x)
except ValueError as ex:
    print("Exception: ", ex)