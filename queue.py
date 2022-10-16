
queue=[]
def enqueue():
    element=input('enter element')
    queue.append(element)
    print(queue)

def dequeue():
    if not queue:
        print('stack is empty')
    else:
        e=queue.pop()
        print(e)
        print(queue)
while True:
    print('enter your choice 1 for push, 2 fro pop , 3 for quit')
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print('wrong choice')