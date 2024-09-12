a = int(input("no of lists? "))
b = int(input("no of elements in each list? "))
mergelist = []

def sort_list(n):
    for i in range(1, len(n)):
        current = n[i]
        pos = i
        while pos > 0 and n[pos - 1] > current:
            n[pos] = n[pos - 1]
            pos -= 1
        n[pos] = current
    return n

for _ in range(a):
    userlist = list(map(int, input("Enter sorted list: ").split()))
    mergelist.extend(userlist)
sortedlist = sort_list(mergelist)
print("Merged & sorted list:", sortedlist)