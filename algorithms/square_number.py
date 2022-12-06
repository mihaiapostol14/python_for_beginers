def square_number(number):
    print(number**2)

try:
    square_number(int(input("Enter number: \n")))
except ValueError:
    print("Enter only number")