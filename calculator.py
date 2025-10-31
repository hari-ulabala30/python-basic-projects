n=int(input())
a=int(input())
b=int(input())
match n:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case 5:
        print("hi")
    case _:
        print("invalid case")    

