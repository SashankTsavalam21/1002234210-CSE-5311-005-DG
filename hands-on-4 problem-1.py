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


'''PS C:\Users\sasha\OneDrive\Documents\GitHub\1002234210-CSE-5311-005-DG>
PS C:\Users\sasha\OneDrive\Documents\GitHub\1002234210-CSE-5311-005-DG> & C:/Users/sasha/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/sasha/OneDrive/Documents/GitHub/1002234210-CSE-5311-005-DG/hands-on-4 problem-1.py"
no of lists? 3
no of elements in each list? 4
Enter sorted list: 1 3 5 7
Enter sorted list: 2 4 6 8
Enter sorted list: 0 9 10 11
Merged & sorted list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
PS C:\Users\sasha\OneDrive\Documents\GitHub\1002234210-CSE-5311-005-DG>''
