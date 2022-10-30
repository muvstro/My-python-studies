chips=3
pasta=1.5
buckwheat=1.2
cola=0.99
name=input("Hello, what's your name? ")
print("Welcome to our store ",name)
sum=0
money=4
while True:
    print("Choose a product: 1-chips,2-pasta,3-buckwheat,4-cola")
    tovar=int(input())
    if tovar==1:
        print("How many packs do you need?")
        col=int(input())
        sum=sum+chips*col
    elif tovar==2:
        print("How many packs do you need?")
        col = int(input())
        sum=sum+pasta*col
    elif tovar==3:
        print("How many packs do you need?")
        col=int(input())
        sum=sum+buckwheat*col
    elif tovar==4:
        print("How many bottles do you need?")
        col=int(input())
        sum=sum+cola*col
    else:
        print("Sorry, we don't have this product!")
    print("Do you want anything else? yes?/no")
    answer=input();
    if answer.lower()== "no":
        break
print(name, "that will be ", sum)
if sum<=money:
    print("Thank you,we will be glad to see you again, " , name,"!")
else: print(name,"sorry, but you don't haveenought money.")

        