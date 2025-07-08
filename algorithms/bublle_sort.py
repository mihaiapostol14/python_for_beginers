from random import randint

# Create generator number

count_numeber = 16  # count numeber in array
write_list = []

# for i in range(count_numeber):
# 	write_list.append(randint(0,800))
# print(write_list)  # this is not sorted list
#
# # Create buble sort

for i in range(count_numeber-1):
	for j in range(count_numeber-i-1):
		if write_list[j] > write_list[j+1]:
			 write_list[j], write_list[j+1] = write_list[j+1], write_list[j]
			 
print(write_list) # "this is sorted list"