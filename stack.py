# stack...........................................

stack=[]
def push():
    element=input('enter element')
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print('stack is empty')
    else:
        e=stack.pop(0)
        print(e)
        print(stack)
while True:
    print('enter your choice 1 for push, 2 fro pop , 3 for quit')
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print('wrong choice')