
"""       --->     <Rock Paper Scissor Game>     <---       """


Tscore=[]
p=int(input("\nEnter How Many Rounds You Wanna Play : "))

n=0
while n<p:
    n+=1
    import random

    def check(user,comp):
        if comp==user:
            return 0
        elif comp==0 and user==2:
            return -1
        elif comp==1 and user ==0:
            return -1
        elif comp==2 and user ==1:
            return -1
        else:
            return 1
    

    comp=random.randint(0,2)
    print(f"{n}-> Round")
    user=int(input("Enter \n0 For Rock \n1 For Paper \n2 For Scissor \nChoose : "))

    if user>=0 and user<=2:
        score=check(user,comp)
    else:
        print("Wrong Input Try Again !!")
        score=0
        continue
       
    if user ==0:
        l="Rock"
    elif user ==1:
        l="Paper"
    elif user ==2:
        l="Scissor"

    if comp ==0:
        v="Rock"
    elif comp ==1:
        v="Paper"
    elif comp ==2:
        v="Scissor"
    
    print("\nYou Choose :",l)
    print("\nComputer Choose :",v)

    if score ==0:
        print("\nIt's Draw !!")
    elif score==-1:
        print("\nYou lose !!")
    else:
        print("\nYou Won !!")
    print("\n--------------------------------")
    Tscore.append(score)

from functools import reduce
Overall_score=reduce(lambda x,y : x+y , Tscore)
print(f"\nYour Score : {Tscore}")
print("\n--------------------------------")
print(f"\nYour Overall_Score in {n} Rounds : {Overall_score}\n")