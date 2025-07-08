def unique_sum(lst):
    if lst == []:
        return None
    else:
        return sum([*set(lst)])


print(unique_sum([1,2,5,3]))