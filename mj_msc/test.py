def integer_to_binary(integer):
    binary = list(bin(integer)[2:].zfill(8))
    return binary

# Example usage:
number = 8
binary_number = integer_to_binary(number)
print(binary_number)

list1 = [0,1,2,3]
list2 = ["a","b","c"]
list1.append(list2)
print(list1)
