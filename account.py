username=input("Enter username: ")
while True:
    password=input("Enter password: ")
    if len(password)<8:
        print("Password is too short")
    elif username in password:
        print("Password contains username: ")
    else:
        print("Password for user",username,"set")
        break    
password2=input("Enter a password again: ")
while True:
    if password2 == password:
        print("Correct")
        break
    else:
        print("Incorrect,try again")

        
