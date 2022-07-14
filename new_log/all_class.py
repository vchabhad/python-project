
import json

ordered_item=[]
class password :
    def __init__(self) -> None:
        self.out_dict={}
        self.dict1={}
        self.list1=[]
        pass
    def pass_check(self,password):
        l, u, p, d = 0, 0, 0, 0
        special="!@#$%^&*()_+"
        for i in password:
            if (i.islower()):
                l+=1      
            if (i.isupper()):
                u+=1     
            if (i.isdigit()):
                d+=1   
            if i in special :
                p+=1

        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
            passflag=1
        return passflag

class user:
    def __init__(self):
        self.out_dict={}
        self.dict1={}
        self.list1=[]
        self.dict2={}

    def  store_user(self,username,phone_no,email,password,address):
        self.out_dict["user_name"]=username
        self.out_dict["user_phone_no."]=phone_no
        self.out_dict["user_email"]=email
        self.out_dict["user_password"]=password
        self.out_dict["user_address"]=address
        self.list1.append(self.out_dict)
        self.dict1["userinfo"]=self.list1
        try:
            with open("userdetails.json","r+")as f:
                j=f.read()
                fs=json.loads(j)
                for i in fs:
                    if i == "userinfo":
                        s=fs[i]
                        s.append(self.out_dict.copy())
                        self.dict1["userinfo"]=s
                        json.dumps(self.dict1,f,indent=4)
                        f.close()
        except:
            with open("userdetails.json","w") as fil:
                fil.write(json.dumps(self.dict1,indent=4))
        
    def validate_admin(self):
            username = input("Enter your email for login  => ")
            password = input("Enter your password for login  => ")
            
            with open('admin_cred.txt', 'r') as f:
                for line in f:
                    if username + ' ' + password + '\n' == line:
                        while True :
                            print('\t\t>>>> 1.Add food item <<<< \n  \t\t>>>> 2.Update food item <<<< \n  \t\t>>>> 3.View food items <<<< \n \t\t>>>> 4.Delete food items <<<< \n \t\t>>>> 5.Exit <<<<')
                            choise= input("Enter your choice  => ")

                            if choise == "1":
                                foodobj.store_food()
                            elif choise == "2":
                                foodobj.update_food_item()
                            elif choise == "3":
                                foodobj.view_food_item()
                            elif choise == "4":
                                foodobj.delete_food_item()
                            elif choise =="5":
                                break
                            else :
                                print("\n\t\t Enter correct choise!!")

                    else :
                        print("Enter correct credentials")
                        return False

    def place_order(self):
        with open("food_details.json","r+") as f:
                    fooddata=json.load(f)
        try:
            if len(fooddata["foodinfo"])!=0:
                print("\n\t\tlist of Availabe Food Items :\n")
                
                menu=[]
                for items in fooddata["foodinfo"]:
                    menu.append([items["food_name"],items["food_quantity"],items["food_price"]])
                for i in range(len(menu)):
                    print(i+1,".",menu[i])
                while True:
                    print("\n\tEnter 1 to Place the Order\n\tEnter 2 to Exit ")
                    x=input("Please Select Your Operation : ")
                    if x=="1":
                        print("Enter the Food number You want to ordered separated by comma")
                        y=input().split(",")
                        for i in y:
                            z=int(i)
                            if z<=len(menu):
                                ordered_item.append(menu[z-1])
                            else:
                                print("\nWe Don't have this Food Item : ",z)
                        print("\n\t\tList of food item you selected : \n")
                        for j in ordered_item:
                            print(j)
                    elif x=="2":
                        break
                    else:
                        print("!! Invalid Number !!\n")
            else:
                print("\n!! Sorry! No Food Items are available Now !!\n")
                        
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!")  

    def ordered_history(self):
        print("\n\t\tList of Previous ordered : \n")
        for i in ordered_item:
            print("\t\t",i)

class food :
    def __init__(self):

        self.out_dict={}
        self.dict1={}
        self.list1=[]
        self.dict2={}

    def store_food(self):
        print("************|Store food|*************\n")
        with open("food_details.json","r+")as f:
                j=f.read()
        foodid=len(j)+1
        
        food_id = str(foodid)
        food_name = input("Enter food name  => " )
        food_quantity = input("Enter quantity for this item(values only)  => ")
        food_price = input("Enter price for this item(in inr only)  =>")
        food_discount = input("Enter discount for this item (values only)  => " )
        food_stock = input("Enter Stock  of this item (values only) => " )
                
        self.out_dict["food_id"]=food_id
        self.out_dict["food_name"]=food_name
        self.out_dict["food_quantity"]=food_quantity
        self.out_dict["food_price"]=food_price
        self.out_dict["food_discount"]=food_discount
        self.out_dict["food_stock"]=food_stock
        self.list1.append(self.out_dict)
        self.dict1["foodinfo"]=self.list1
        print("\n\t\t Item added sucessfully.")

        try:
            with open("food_details.json","r+")as f:
                j=f.read()
                fs=json.loads(j)
                for i in fs:
                    if i == "foodinfo":
                        s=fs[i]
                        s.append(self.out_dict.copy())
                        self.dict1["foodinfo"]=s
                        json.dumps(self.dict1,f,indent=4)
                        f.close()
        except:
            with open("food_details.json","w") as fil:
                fil.write(json.dumps(self.dict1,indent=4))


        
    def update_food_item(self):
        try:
            x=input("Enter the Food ID you want to update => \n")
            with open("food_details.json","r+") as f :
                food_data=json.load(f)
            for dics in food_data['foodinfo']:

                if dics['food_id']==x:
                    

                    print("\t\t>>>>1. Update Food Name <<<<\n \t\t>>>> 2. Update Quantity <<<<\n \t\t>>>>3. Update Price <<<<\n \t\t>>>> 4. Update Discount <<<<\n\t\t>>>> 5. Update Stock <<<< \n ")
                    y= input("Enter your choice : ")
                    if y=="1":
                        updated_food_name=input("Enter new name: ")
                        dics['food_name']=updated_food_name
                        print("\n!! Successfully Updated !!\n")
                        break

                    elif y=="2":
                        updated_food_quantity=input("Enter new Quantity: ")
                        dics['food_quantity']=updated_food_quantity
                        print("\n!! Successfully Updated !!\n")
                        break
                    elif y=="3":
                        updated_food_price=input("Enter new Price: ")
                        dics['food_price']=updated_food_price
                        print("\n!! Successfully Updated !!\n")
                        break
                    elif y=="4":
                        updated_food_discount=input("Enter new discount: ")
                        dics['food_discount']=updated_food_discount
                        print("\n!! successfully Updated !!\n")
                        break
                    elif y=="5":
                        updated_food_stock=input("Enter new stock: ")
                        dics['food_stock']=updated_food_stock
                        print("\n!! Successfully Updated !!\n")
                        break
                    else:
                        print("!! Sorry Invalid Number !!\n")
                        break
            
        
            
            with open("food_details.json","w+")as s:
                json.dump(food_data,s,indent=4)
                
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")  
            
            
    def view_food_item(self):
        with open("food_details.json","r+") as f:
            food_data=json.load(f)

        print("List of Food Items : \n")
        if len(food_data['foodinfo'])!=0:    
            for dics in food_data['foodinfo']:
                print(dics)
        else:
            print("!! Sorry No Food Items  Added !!\n")
            

    def delete_food_item(self):
        with open("food_details.json","r+") as f:
            food_data=json.load(f)
        try:

            print("Enter the Food ID which you want to delete:")
            choise=input()

            for i in range(len(food_data['foodinfo'])):
                if food_data['foodinfo'][int(i)]['food_id'] == str(choise):
                    del food_data['foodinfo'][i]
                    break

            print("\n!! Food item deleted successfully !!\n")
            

            with open("food_details.json","w+")as s:
                json.dump(food_data,s,indent=4)
            
        except Exception as e:
            print("\n!! Please Provide Valid Inputs !!\n")    








class update_details:
    
    def update_profile(self,email):
        with open("userdetails.json","r+")as f:
            users_data = json.load(f)
        for dics in users_data['userinfo']:
            if dics['user_email']== email:
                updated_username=input("Enter New username: ")
                updated_phone_no=input("Enter new phone number: ")
                updated_address=input("Enter new Address: ")
                dics['user_name'] = updated_username
                dics['user_phone_no.'] = updated_phone_no
                dics['user_address'] = updated_address
                break

        with open("userdetails.json","w+")as s:
            json.dump(users_data,s,indent=4)


foodobj=food()
updatedetailsobj=update_details()               
passobj=password()
userobj=user()
