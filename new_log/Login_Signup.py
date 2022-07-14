import json
from all_class import *
import os
import datetime

navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 

    
out_dict={}
dict1={}
list1=[]

def signup():
    print("************|welcome to signup Page|*************\n")
    username = input("Enter your username => " )
    phone_no = input("Enter your phone_number  => " )
    email = input("Enter your email  => ")
    address = input("Enter your address  =>")
    password = input("Enter your password  => " )
    
    if passobj.pass_check(password)==1:
        print("Password valid. Please re enter the password to confirm")
    
        password2=input("Enter your confirm password  => ")
        if password==password2:
            print("\n****|-->  You Signed Up Succsefully  <--|****")
            userobj.store_user(username,phone_no,email,password,address)
            
        else:
            print("\n****|-->  both password are wrong  <--|****")
    else:
        print("invalid")
    
def login():
    i=0
    k=0
    while 1: 
        email = input("Enter your email for login  => ")
        password = input("Enter your password for login  => ")

        with open("userdetails.json",'r') as fd:
            users_data = json.load(fd)

        for dics in users_data['userinfo']:
            if dics['user_email']==email and dics['user_password']==password:
                print()
                print("|succesfully logged IN|")
                k = 1
                
        if k == 1:
            while True:
                print('\t\t>>>> 1.Place order <<<< \n  \t\t>>>> 2.Get report or history <<<< \n  \t\t>>>> 3.Update profile <<<< \n  \t\t>>>> 4.Exit <<<<')
                choise= input("Enter your choice  => ")

                if choise== "1":
                    userobj.place_order()
                elif choise=="2":
                    userobj.ordered_history()
                
                elif choise == "3":
                    print('\t\t>>>> Enter new details <<<<')
                    updatedetailsobj.update_profile(email)
                    print("\t\tProfile  updated Successfully.")

                elif choise =="4":
                    break
    

            break

            

            
        elif i == 3:
            print("\n\t\t****|--> User Not found <--|****\n")
            break
        else:
                print("\n\t\t****|--> <--- Wrong password! Please try again. <--|****\n")
        i+=1
            
def update_profiles():
    updatedetailsobj.update_profile()
def Admin_login():
    userobj.validate_admin()

    
def main(user):
    if user=="1" or user=="signup" :
        signup()
        b=input("\nDo you want login(1) or Exit(2)  => ")
        if b == "1":
            login()
        else:
            print("****|--> Thanks for your precious time <--|****")
    elif  user=="2" or user=='login':
        login()
    
    elif user=='3' or user=='admin login' :
        Admin_login()

        
    else:
        print("****|--> unvalid operation <--|****")


if __name__ == "__main__":
    while True :
        print('\n**********|->>> welcome in my websites <<<-|************\n')
        print('\t\t>>>> 1.SIGNUP <<<< \n  \t\t>>>> 2.Login <<<< \n  \t\t>>>> 3.ADMIN LOGIN <<<< \n  ')
        user_input = input("Would you want to login/signup => ")
        main(user_input)

    
