"""import random
def number():
    number_guess=random.randint(1,100)
    attempts=0
    while True:
        try:
            guess=int(input())
        except ValueError as e:
            print(e)
        attempts+=1
        if guess<number_guess:
            print("to low")
        if guess>number_guess:
            print("to high")
        else:
            print(f"found{attempts}")   
            break    
number()              """       
def guessnumber(start,end):
    if start>end:
        print("number not found")
        return
    mid=(start+end)//2
    print(f"is the {mid} numeber(Y/N):")
    user=input().strip()
    if user in ("Y","y"):
        print(f"found succesfull{mid}")
    elif user in ("N","n"):
        print(f"is the number greater than {mid} (Y/N):")
        user=input().strip()
        if user in ("Y","y"):
            return guessnumber(mid+1,end)
        elif user in ("N","n"):
            return guessnumber(start,mid-1)
        else:
            return guessnumber(start,end)
        
    else:
         return guessnumber(start,end)  
guessnumber(1,100)                  


