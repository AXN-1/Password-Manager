import random 
import string

password={}

#load existing password file
try:
    with open ("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            password[website] = pwd
except:
    pass
def generate_password():
    char = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    password = "".join(random.choice(char) for _ in range(8))
    return password
while True:
    print("/n-----PERSONAL PASSWORD MANAGER-----")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Exit")

    choice=input("Enter your choice: ")

    #Save Password
    if choice == "1":
        site = input("Enter site: ")
        pwd = input("Enter Password: ")
        password[site] = pwd
        with open ("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")
        print("Saved!")
    
    #View Password
    elif choice == "2":
        if not password:
            print("Password not found")
        else:
            print(site, ":", pwd)
    
    #Generate Password
    elif choice == "3":
        print("Successfully Generated Password!!")
        print("Generated Password:",generate_password())

        
    #Exiting
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")