def sort_and_prod():
    for i in range(1, 10):
        for z in range(i, 10):
            for t in range(z, 10):
                prod = i*z*t
                print(prod)

functions = sort_and_prod()
print(functions)
