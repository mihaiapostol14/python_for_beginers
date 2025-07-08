def arithmetic(a, b, operator):
    if 'add' in operator:
        result = a+b
        print(f'{a},{b} ----> "{operator}" ----> {result} ')

    if 'subtract' in operator:
        result = a-b
        print(f'{a},{b} ----> "{operator}" ----> {result} ')

    if 'multiply' in operator:
        result = a*b
        print(f'{a},{b} ----> "{operator}" ----> {result} ')

    if 'divide' in operator:
        result = round(a/b)
        print(f'{a},{b} ----> "{operator}" ----> {result} ')


arithmetic(a=1, b=2, operator='add')
arithmetic(a=8, b=2, operator='subtract')
arithmetic(a=5, b=2, operator='multiply')
arithmetic(a=8, b=2, operator='divide')
