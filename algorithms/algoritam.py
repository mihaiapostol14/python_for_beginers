def algoritam(array):
    number_1 = [number1 for number1 in array if number1 % 2 == 0 and number1 % 4 == 0]
    number_2 = [number2 for number2 in array if number2 % 2 != 0 and number2 % 4 != 0]

    print(f"this is divide with 2: {number_1}")
    print(f"this is not divide with 2: {number_2}")


algoritam(array=tuple(range(1,10)))