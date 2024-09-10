def extra(length):
    x = 1
    for _ in range(length * length):
        x += 1
        _ = _ % length
    return x
def basic(length):
    x = 1
    for _ in range(length* length):
        x += 1
    return x

result_extra = extra(4)
result_basic = basic(4)

print("Result of extra:", result_extra)
print("Result of basic:", result_basic)