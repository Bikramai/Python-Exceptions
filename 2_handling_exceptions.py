
try:
    age = int(input('age:'))
except ValueError:
    print("You didn't enter a valid age.")
else: 
    print("No exceptions were throw.")
print("Execution continues.")
print('\n')


# optional method to handling exceptions
try:
    age = int(input('age:'))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))


