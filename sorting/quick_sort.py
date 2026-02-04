def quick_sort(lst, start, end):
    if end <= start:
        return
    
    pivot = partition(lst, start, end)
    quick_sort(lst, start, pivot - 1)
    quick_sort(lst, pivot + 1, end)
    

def partition(lst, start, end):
    pivot = lst[end]
    j = start
    i = start - 1

    while j <= (end - 1):
        if lst[j] < pivot:
            i += 1
            lst[j], lst[i] = lst[i], lst[j]
        j += 1

    i += 1
    lst[i], lst[end] = lst[end], lst[i]
    return i

#l = [1,3,5,7,2,4,6,8]
#quick_sort(l, 0, len(l) - 1)
#print(l)


list1 = [32,10,4,6,99,80,11]
list2 = [9]
list3 = [9, 11, 10]
list4 = [1, 2, 4, 6, 5]
list5 = []
lists = [list1, list2, list3, list4, list5]

for i in lists:
    quick_sort(i, 0, len(i) - 1)
    print(i)