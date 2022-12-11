#raise
try:
    data = int(input("Please enter a number: "))
    if data == 10:
        print("Activating exception")
        raise ZeroDivisionError
    else:
        raise TypeError
except ZeroDivisionError:
    print("From Zero Division Error")
except TypeError:
    print("From Type Error")

