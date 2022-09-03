username=input("Enter username")
password=input("Enter password")
while True:
    if len(password)<8:
        print("Password is too short")
    elif username in password:
        print("Password contains username")
    else:
        print("Password for user",username,"set")
    break
password=input("Enter password again")
        
            
