for number_x in range(10,25):
    for number_y in range(10, 25):
        if number_x != number_y:

            r1 = 0
            r2 = 0

            for i in range(1,number_x + 1):
                if number_x %i == 0:
                    r1 += i

            for i in range(1,number_y + 1):
                if number_y %i == 0:
                    r2 += i

            if r1 == r2:
               print(number_x,number_y)
