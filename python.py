#1
current_number = 0
while current_number <= 5:
    print(current_number)
    current_number += 1
    
#2
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))
#3
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))
#4
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    count = 0
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(output)
    return output
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
#5
def length_and_value(size, value):
    output = []
    for i in range (0 , size):
        output.append(value)
    return output
print(length_and_value(4,7))
print(length_and_value(6,2))
