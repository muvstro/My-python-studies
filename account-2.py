username=input("Enter username")
password=input("Enter password")
retries=3
while True:
    if len(password)<8:
        print("Password is too short")
    elif username in password:
        print("Password contains username")
    else:
        print("Password for user",username,"set")
        break 
password2=input("Enter a password again")
while retries>0:
    if password2 == password:
        print("Correct")
    else:
        retries=retries-1
    
        print("Incorrect,try again")
        
                


