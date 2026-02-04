def binary_search(lst, left, right, n):
    if left <= right:
        mid = (left + right)//2
        if lst[mid] == n:
            return mid
        elif lst[mid] < n:
            return binary_search(lst, mid + 1, right, n)
        else:
            return binary_search(lst, left, mid - 1, n)
    else:
        return -1
    
def binary_search_interative(lst, n):
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == n:
            return mid
        elif lst[mid] > n:
            right = mid - 1
        elif lst[mid] < n:
            left = mid + 1
            
    return -1
            
list1 = [1, 3, 5, 6, 8, 9, 10, 32]
list2 = [9]
list3 = [9, 11]
list4 = [1, 2, 4, 5]
list5 = []
lists = [list1, list2, list3, list4, list5]

for i in lists:
    print(binary_search(i, 0, len(i) - 1, 9), binary_search_interative(i, 9))