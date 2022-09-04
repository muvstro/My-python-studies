username=input("Enter username: ")
retries=3
while True:
    password=input("Enter password: ")
    if len(password)<8:
        print("Password is too short")
    elif username in password:
        print("Password contains username: ")
    else:
        print("Password for user",username,"set")
        break    
while retries>0:
    password2=input("Enter a password again: ")
    if password2 == password:
        print("Correct")
        break
    else:
        print("Incorrect,try again")
        retries=retries-1
if retries==0:
    print("retries are over") 

        