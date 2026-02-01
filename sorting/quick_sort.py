def merge_sort(lst):
    n = len(lst)
    
    if (n <= 1): 
        return
    
    middle = n//2
    left, right = [], []
    
    for i in range(n):
        if i < middle:
            left.append(lst[i])
        else:
            right.append(lst[i])
    #print(middle, left, right)            
    merge_sort(left)
    merge_sort(right)
    merge(left, right, lst)
    return lst
    
def merge(left, right, lst):
    lsize, rsize = len(left), len(right)
    l, r, i = 0, 0, 0
    
    while(l < lsize and r < rsize):
        if left[l] <= right[r]:
            lst[i] = left[l]
            i += 1
            l += 1
        else:
            lst[i] = right[r]
            i += 1
            r += 1
            
    while(l < lsize):
        lst[i] = left[l]
        i += 1
        l += 1
        
    while(r < rsize):
        lst[i] = right[r]
        i += 1
        r += 1
    
#l = [1,3,5,7,2,4,6,8]
#print(merge_sort(l))

list1 = [32,10,4,6,99,80,11]
list2 = [9]
list3 = [9, 11, 10]
list4 = [1, 2, 4, 6, 5]
list5 = []
lists = [list1, list2, list3, list4, list5]

for i in lists:
    merge_sort(i)
    print(i)