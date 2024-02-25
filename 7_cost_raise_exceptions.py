from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
  
    pass # pass statement is the statement that doesn't do anything
"""
print('\n')

# This second approch almost 4X faster than the above code
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age



    xfactor = calculate_xfactor(-1)
    if xfactor == None:
        pass

"""

print('first code=', timeit(code1, number=10000))
print('second code=', timeit(code2, number=10000))


#Note:-
# if you are building simple application for few users raising exceptions
# in function is not gonna have not bad impact on the performance on your 
# applications.But If you are building application where performance and 
# scalability is important. It's better to raise exceptions when you really
# have too.

# As a general role of thumb, when you raise exceptions in your functions
# think twice. See if you can handle the suitation with simple if statements.
# whether there is performance different or not code will end of with little bit cleaner.
 