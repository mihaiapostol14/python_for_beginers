def multiplication_table(number: int, ran: int):
    for n in range(1, number + ran - 1):
        statement = f'{number} x {n} = {number * n}'
        print(statement)


for i in range(1, 14):
    multiplication_table(number=i, ran=i)
