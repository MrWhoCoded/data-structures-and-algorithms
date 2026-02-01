def bubble_sort(lst, n):
    if n == 0 or n == 1:
        return lst
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j + 1] < lst[j]:
                #print(lst[j])
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst

list1 = [32,10,4,6,99,80,11]
list2 = [9]
list3 = [9, 11, 10]
list4 = [1, 2, 4, 6, 5]
list5 = []
lists = [list1, list2, list3, list4, list5]

for i in lists:
    print(bubble_sort(i, len(i)))