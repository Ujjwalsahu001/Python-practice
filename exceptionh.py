#EXCEPTION HANDLING---------------
#TRY CATCH EXCEPT FINALLY
# ZERO DIVISION 
try:
    numerator = float(input("Enter the value: "))
    denominator = float(input("Enter the value: "))

    # attempt division

    result = numerator/denominator
    print(f"REsult:{result}")
except ZeroDivisionError:

    # this run only if the user nters 0 as the second number
    print("Error: you can't divide by zero...")

except ValueError:
    print("Error:Please enter a vailed number...")