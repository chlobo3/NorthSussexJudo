name = "Coach"
password = "BestJudo!10"

name_entry = input("enter your name: ") 
password_entry = input("enter your password: ")

if (name_entry + password_entry == name + password):
    print("login succesful")
else: 
    print("login unsuccesful")

