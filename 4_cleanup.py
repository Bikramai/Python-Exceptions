try:
    file = open("app.py")
    age = int(input('age:'))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else: 
    print("No exceptions were throw.")
finally:
    file.close()