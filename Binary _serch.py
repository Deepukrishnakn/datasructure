#binary serch---------------------------------------------------

def binary_serch(list1,key):
    low = 0
    high = len(list1)-1
    found=False
    while low<=high and not found:
        mid=(high+low)//2
        if key == list1[mid]:
            found =True
        elif key > list1[mid]:
            low = mid+1
        else:
            high = mid-1
    if found == True:
        print(key,'found')
    else:
        print('not found')

list1=[2,3,452,11,66,4,0]
list1.sort()
key=int(input('enyer key'))
binary_serch(list1,key)
print(list1)