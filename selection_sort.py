# ith using min and max methods

# list1=[2,3,5,5,3,33,70]
# print(list1)
# for i in range(len(list1)-1):
#     min_val = max(list1[i:])
#     min_index = list1.index(min_val,i)
#     if list1[i] != list1[min_index]:
#         list1[i],list1[min_index] = list1[min_index],list1[i]
#         print(list1)

#--------------------------------------------------------------------------------

list1=[22,35,50,5,3,33,70]
print(list1)
for i in range(len(list1)-1):
    min_index = i
    for j in range(i+1,len(list1)):
        if list1[j] > list1[min_index]:
            min_index = j

    if list1[i] != list1[min_index]:
        list1[i],list1[min_index] = list1[min_index],list1[i]
        print(list1)