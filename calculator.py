#######Calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def main():
    a=int(input('give a'))
    b=int(input('give b'))

    choice=input('add/sub/mal')
    if choice =='add':
        print(add(a,b))
    elif choice=='sub':
        print(sub(a,b))
    else:
        print(mul(a,b))

main()
