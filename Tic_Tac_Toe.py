from tabulate import tabulate
import random
import os

def clear_screen():
    # If the system is Windows, run 'cls', otherwise run 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')
c=True
while c:
    L=[[" "," "," "], [" "," "," "], [" "," "," "]]
    i=input("Player 1 enter choice X or O:")
    i=i.upper()
    j=""
    if i=="X":
        j="O"
    else:
        j="X"
    ht=int(input("Player 1 enter 1 for Heads and 2 for Tails:"))
    r=random.randint(1,2)
    b=False
    if ht==r:
        a=input("Enter Player 1 name:")
        k=input("Enter Player 2 name:")
        b=True
    else:
        a=input("Enter Player 2 name:")
        k=input("Enter Player 1 name:")
    print(L)
    D={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
    if b==True:
        while True:
            if L[0][0]==j and L[0][1]==j and L[0][2]==j:
                print(k," won")
                break
            elif L[1][0]==j and L[1][1]==j and L[1][2]==j:
                print(k," won")
                break
            elif L[2][0]==j and L[2][1]==j and L[2][2]==j:
                print(k, "won")
                break
            elif L[0][0]==j and L[1][0]==j and L[2][0]==j:
                print(k," won")
                break
            elif L[0][1]==j and L[1][1]==j and L[2][1]==j:
                print(k," won")
                break
            elif L[0][2]==j and L[1][2]==j and L[2][2]==j:
                print(k," won")
                break
            elif L[0][0]==j and L[1][1]==j and L[2][2]==j:
                print(k," won")
                break
            elif L[0][2]==j and L[1][1]==j and L[2][0]==j:
                print(k," won")
                break
            while True:
                d=int(input("Enter integer where you want your symbol placed:"))
                if L[D[d][0]][D[d][1]]==" ":
                    clear_screen()
                    L[D[d][0]][D[d][1]]=i
                    break
                else:
                    print("Block Occupied.Try Again!")
            print(tabulate(L,tablefmt="grid"))
            if L[0][0]==i and L[0][1]==i and L[0][2]==i:
                print(a," won")
                break
            elif L[1][0]==i and L[1][1]==i and L[1][2]==i:
                print(a," won")
                break
            elif L[2][0]==i and L[2][1]==i and L[2][2]==i:
                print(a, "won")
                break
            elif L[0][0]==i and L[1][0]==i and L[2][0]==i:
                print(a," won")
                break
            elif L[0][1]==i and L[1][1]==i and L[2][1]==i:
                print(a," won")
                break
            elif L[0][2]==i and L[1][2]==i and L[2][2]==i:
                print(a," won")
                break
            elif L[0][0]==i and L[1][1]==i and L[2][2]==i:
                print(a," won")
                break
            elif L[0][2]==i and L[1][1]==i and L[2][0]==i:
                print(a," won")
                break
            elif " " not in L[0] and " " not in L[1] and " " not in L[2]:
                print("IT'S A DRAW!!")
                break
            while True:
                d=int(input("Enter integer where you want your symbol placed:"))
                if L[D[d][0]][D[d][1]]==" ":
                    clear_screen()
                    L[D[d][0]][D[d][1]]=j
                    break
                else:
                    print("Block Occupied.Try Again!")
            print(tabulate(L,tablefmt="grid"))
    else:
        while True:
            if L[0][0]==i and L[0][1]==i and L[0][2]==i:
                print(k," won")
                break
            elif L[1][0]==i and L[1][1]==i and L[1][2]==i:
                print(k," won")
                break
            elif L[2][0]==i and L[2][1]==i and L[2][2]==i:
                print(k, "won")
                break
            elif L[0][0]==i and L[1][0]==i and L[2][0]==i:
                print(k," won")
                break
            elif L[0][1]==i and L[1][1]==i and L[2][1]==i:
                print(k," won")
                break
            elif L[0][2]==i and L[1][2]==i and L[2][2]==i:
                print(k," won")
                break
            elif L[0][0]==i and L[1][1]==i and L[2][2]==i:
                print(k," won")
                break
            elif L[0][2]==i and L[1][1]==i and L[2][0]==i:
                print(k," won")
                break
            while True:
                d=int(input("Enter integer where you want your symbol placed:"))
                if L[D[d][0]][D[d][1]]==" ":
                    clear_screen()
                    L[D[d][0]][D[d][1]]=j
                    break
                else:
                    print("Block Occupied.Try Again!")
            print(tabulate(L,tablefmt="grid"))
            if L[0][0]==j and L[0][1]==j and L[0][2]==j:
                print(a," won")
                break
            elif L[1][0]==j and L[1][1]==j and L[1][2]==j:
                print(a," won")
                break
            elif L[2][0]==j and L[2][1]==j and L[2][2]==j:
                print(a, "won")
                break
            elif L[0][0]==j and L[1][0]==j and L[2][0]==j:
                print(a," won")
                break
            elif L[0][1]==j and L[1][1]==j and L[2][1]==j:
                print(a," won")
                break
            elif L[0][2]==j and L[1][2]==j and L[2][2]==j:
                print(a," won")
                break
            elif L[0][0]==j and L[1][1]==j and L[2][2]==j:
                print(a," won")
                break
            elif L[0][2]==j and L[1][1]==j and L[2][0]==j:
                print(a," won")
                break
            elif " " not in L[0] and " " not in L[1] and " " not in L[2]:
                print("IT'S A DRAW!!")
                break
            while True:
                d=int(input("Enter integer where you want your symbol placed:"))
                if L[D[d][0]][D[d][1]]==" ":
                    clear_screen()
                    L[D[d][0]][D[d][1]]=i
                    break
                else:
                    print("Block Occupied.Try Again!")
            print(tabulate(L,tablefmt="grid"))
    t=input("Do you want to continue? Y for yes, else we assume no")
    if t in "Yy":
        c=True
    else:
        c=False
