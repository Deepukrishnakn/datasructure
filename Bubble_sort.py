list1=[34,5,22,1,88,6,0]

for j in range(len(list1)-1,0,-1):
    for i in range(j):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1], list1[i]
            print(list1)
        else:
            print(list1)
    print()