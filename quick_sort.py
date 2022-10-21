# to get the currect position of pivot --------------------------------------------------
# tack first element as a pivot 

def pivot_place(list1,first,last):
    pivot = list1[first]
    left = first+1
    rigth = last
    while True:
        while left <= rigth and list1[left] <= pivot:
            left = left+1
        while left <= rigth and list1[rigth] >= pivot:
            rigth = rigth-1
        if rigth < left:
            break
        else:
            list1[left],list1[rigth]=list1[rigth],list1[left]
    list1[first],list1[rigth]=list1[rigth],list1[first]
    return rigth

def quick_sort(list1,first,last):
    if first<last:
        p = pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)

list1 = [33,5,44,8,12,90,3,1]
n=len(list1)
quick_sort(list1,0,n-1)
print(list1)



# last element take as a pivot 


def pivot_place(list1,first,last):
    pivot = list1[last]
    left = first
    rigth = last-1
    while True:
        while left <= rigth and list1[left] <= pivot:
            left = left+1
        while left <= rigth and list1[rigth] >= pivot:
            rigth = rigth-1
        if rigth < left:
            break
        else:
            list1[left],list1[rigth]=list1[rigth],list1[left]
    list1[last],list1[left]=list1[left],list1[last]
    return left

def quick_sort(list1,first,last):
    if first<last:
        p = pivot_place(list1,first,last)
        quick_sort(list1,first,p-1)
        quick_sort(list1,p+1,last)

list1 = [33,5,44,8,12,90,3,1]
n=len(list1)
quick_sort(list1,0,n-1)
print(list1)
