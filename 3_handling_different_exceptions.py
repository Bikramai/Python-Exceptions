try:
    age = int(input('age:'))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be 0.")
else: 
    print("No exceptions were throw.")
print('\n')



# multiple types of exceptions
try:
    age = int(input('age:'))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else: 
    print("No exceptions were throw.")