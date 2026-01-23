try:
    list = [1, 2, 3]   
    print(list[5])
    print(a)
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except (NameError, IndexError):
    print("Variable 'a' is not defined or list index out of bounds.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Division successful.")
finally:
    print("Execution completed.")
