try:
    x,y = eval(input("Enter 2 numbers, sperated by a comma: "))
    result = x/y
    print ("Result is,", result)
except ZeroDivisionError:
    print("Numbers can't be divided by 0!!")
except SyntaxError:
    print("No commas")
except:
   print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will happen no matter what")