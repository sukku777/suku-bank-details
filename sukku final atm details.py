database={'saikrishna':{'name':'krishna','age':21,'email':'chhifdjdfk@gmail.com','password':'sai@9899','amount':20000},'sukumar':{'name':'sukku','age':22,'email':'slfndkfnofnsd@gmail.com','password':'sukumarr','amount':10000}}
print("1.sign in\n2.Sign Up\n3.Exit")
Input=int(input("Enter your Choice :"))
if(Input==1):
    x=database['saikrishna']['name']
    y=database['saikrishna']['password']
    u=database['sukumar']['name']
    v=database['sukumar']['password']
    a=input('enter the username:')
    b=input('enter the password:')
    if((a==x)and(b==y)):
           print('welcome to saikrishna')
           print('Enter your choice:')
           print('1.check balance\n2.Deposit balance\n3.Withdrawl\n4.Log out')
           while True:
               amount=database['saikrishna']['amount']
               z=int(input('enter your choice:'))
               if(z==1):
                   print("Account balance:",amount)
                   another=input('do u want another transaction?yes/no')
                   if another=='yes':
                       continue
                   else:
                       break
               elif(z==2):
                   deposit=int(input('enter the deposit amount:'))
                   Total_amount=amount+deposit
                   print(deposit,'is credited to your account')
                   print('Account balance is:',Total_amount)
               #database.update({'amount':Total_amount})
               elif(z==3):
                    withdraw=int(input('Enter the amount:'))
                    if(amount>withdraw):
                        Total=amount-withdraw
                        print(withdraw,'is debited from your account')
                        print('Account balance is',Total)
                    else:
                        print('Insufficient balance')   
               elif(z==4):
                   print('Log out sucessfully')
               else:
                   print('invalid choice')
    elif((a==u)and(b==v)):
           print('welcome to sukumar')
           print('Enter your choice:')
           print('1.check balance\n2.Deposit balance\n3.Withdrawl\n4.Log out')
           while True:
               amount=database['sukumar']['amount']
               z=int(input('enter your choice:'))
               if(z==1):
                   print("Account balance:",amount)
                   another=input('do u want another transaction?yes/no')
                   if another=='yes':
                       continue
                   else:
                        break   
               elif(z==2):
                   deposit=int(input('enter the deposit amount:'))
                   TOtal_amount=amount+deposit
                   print(deposit,'is credited to your account')
                   print('Account balance is:',Total_amount)
               elif(z==3):
                   withdraw=int(input('Enter the amount:'))
                   if(amount>withdraw):
                       Total=amount-withdraw
                       print(withdraw,'is debited from your account')
                       print('Account balance is',Total)
                   else:
                       print('Insufficient balance')         
               elif(z==4):
                   print('Log out sucessfully')
               else:
                   print('invalid choice')
    elif a==x and b!=y:
        print('invalid password')
        newpassword=input('forgot password?yes/no')
        if newpassword=='yes':
            database['saikrishna']['password']=input('enter the new password')
        else:
            print('exit')
    elif a==u and b!=v: 
        print('invalid password')
        newpassword=input('forgot password?yes/no')
        if newpassword=='yes':
            database['sukumar']['password']=input('enter the new password')
        else:
            print('exit')
    else:
        print('invalid username')
elif(Input==2):
    
    user_name= input('user name:')
    name=input("Enter your name:")
    age=int(input("enter age:"))
    email=input("Enter your email:")
    balance=int(input('enter the amount:'))
    print('Account is created')   
elif(Input==3):
    print("exit")
else:
    print("Invalid Choice")

