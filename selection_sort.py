list1=[2,3,5,5,3,33,70]
print(list1)
for i in range(len(list1)):
    min_val = max(list1[i:])
    min_index = list1.index(min_val,i)
    list1[i],list1[min_index] = list1[min_index],list1[i]
print(list1)