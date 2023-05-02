#database have data related to id & pwd
username = "mann"
password = "mann123"

#start code for login page

user = input("Enter U_Name : ")
if user == username:
    ps = input ("Enter Password : ")
    if ps == password:
        print("Login Sucessful")
    else:
        print("Enter Valid Password")
else: 
    print("Enter Valid Username")
