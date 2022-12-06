def equal_list(actual_list, initial_list: list) -> list:
    if len(set(actual_list)) == initial_list:
        return (f'list {actual_list} not is equal with list {initial_list}')
    else:
        return (f'list {actual_list} is equal with list {initial_list}')


test_1 = equal_list(actual_list=[1,2,4,4,4,5,5], initial_list=[1,2,4,5])
test_2 = equal_list(actual_list=[1,2,3,4], initial_list=[1,2,3,4])

print(test_1)
print(test_2)
