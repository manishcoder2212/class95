def selectScreen():
    print("click 1 for home screen")
    print("click 2 for regester screen")
    print("click 3 for transaction screen")
    v=int (input('select the number'))

    if (v==1):
        screen1()
    elif(v==2):
        screen2()
    else:
        screen3()



def screen1():
    print("you are in the home Screen")
    
    
def screen2():
    print("you are in the regester Screen")
    x=input("enter your name")
    a=input("enter your contact number")
    b=input("enter your address")
    print("yhhh 🥳🥳🥳🥳🥳 you done th regestration")

def screen3():
    print("you are in the Transaction Screen")
    s=input("id of costume")
    q=input("amount to pay")
    print("yhh🥳🥳🥳🥳🥳 you transaction for  "+s +"  of price "+q+"  is under process")

selectScreen()