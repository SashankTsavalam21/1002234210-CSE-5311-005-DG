def elimination(array):
    if len(array) == 0:
        return []
    
    result = []
    
    for x in array:
        if not result or result[-1] != x:
            result.append(x)
    
    return result

userinput = input("Enter a sorted sequence of numbers separated by spaces: ")
num = list(map(int, userinput.split()))

unique_num = elimination(num)

print("starting list:", num)
print("after removing duplicates:", unique_num)