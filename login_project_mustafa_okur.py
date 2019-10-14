#!/usr/bin/env python
# coding: utf-8

# In[4]:



# this is a project about login system
print("Welcome to the real world!!!")
users ={}


def oldmember():
    name = input("Please enter your username : ")
    password = input("please enter your password.")
    if users[name]==password:
        print("Login is succesful")
    else:
        print("At least  one of the data you entered is wrong. Please try again")
        oldmember()


def newmember():
    print("YOU NEED TO SIGN UP TO ACCES TO THE SITE\n")
    username = input("Please enter a username : ")
    if username in users.keys():
        print("this username was taken, try another username \n")
    password1 = input("please enter a password : ")
    password2 = input("please confirm the password :")
    if password1 == password2:
        users[username]=password1
        print('SIGN UP IS SUCCESFULL\n')
        oldmember()
    else:
        print("Passwords doesn't match. Try again \n")
        newmember()
def main():
    
    status = input("Are you a member? y/n \n")
    status = status.lower()

    if status == "y":
        oldmember()

    elif status == "n":
        newmember()

    else:
        print('only "y" or "n" \n')
        main()
main()


# In[ ]:





# In[ ]:




