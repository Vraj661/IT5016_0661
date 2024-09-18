'''
PROGRAM WHICH IS LISTS
NAME VRAJ PRAJAPATI
'''

my_list = [1,2,3,"Apple","Lemon"]

first_element = my_list[0]
print(first_element)

my_list[2]="Watermelon"  # to change value
print(my_list)

# append
my_list.append(6)      # to insert the value 
print(my_list)

# insert
my_list.insert(2, 5)  # to insert the value at the specified position
print(my_list)

# remove
my_list.remove(2)  # to remove value
print(my_list)

# pop
poped_element = my_list.pop()  # to remove value at the specified position
print(my_list)

# sort
my_list.sort(key=str) # sorts the list
print(my_list)

# reverse
my_list.reverse()
print(my_list)