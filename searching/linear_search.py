def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

lists = [
    [3, 5, 6, 8, 9, 10, 32, 1],
    [9],
    [9, 11],
    [1, 2, 4, 5]
]

for lst in lists:
    print(linear_search(lst, 9))
