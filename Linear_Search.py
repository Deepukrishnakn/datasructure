def linearserch(list1,key):
    flag=False
    list2=[]
    for i in range(len(list1)):
        if list1[i]==key:
            flag=True
            list2.append(i)
    if flag==True:
        
        for i in list2:
            print('key is found index is:',i,",")
    else:
        print('key is not found')


list1=[22,1,4,34,51,0,34,33,33,22]
key=int(input('enter key'))
linearserch(list1,key)

        