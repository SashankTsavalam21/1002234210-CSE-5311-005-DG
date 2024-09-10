def list(lst):
    if len(lst) > 1:
        middle = len(lst) // 2
        l = lst[:middle]
        r = lst[middle:]

        list(l)
        list(r)

        merge(lst, l, r)

def merge(lst, l, r):
    a = b = c = 0
    for c in range(len(lst)):
        if a < len(l) and (b >= len(r) or l[a] <= r[b]):
            lst[c] = l[a]
            a += 1
        else:
            lst[c] = r[b]
            b += 1
ex = [5, 2, 4, 7, 1, 3, 2, 6]
print("given array:", ex)
list(ex)
print("sortted array:", ex)