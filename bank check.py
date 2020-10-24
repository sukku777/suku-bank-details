users={'suku101':{'name':'suku','age':22,'email':'sukumar.cje0nu@gmail.com','password':'suku1','amount':20000},'sai121':{'name':'sai','age':21,'email':'suku123@gmail.com','password':'sai123','amount':10000}}
status= ""
#def displayMenu():
#    status = input("Are you a registered user? y/n? Press q to quit: ")  
 #   if status == "y":
  #      oldUser()
   # elif status == "n":
    #    newUser()
def signup():
    createLogin = input("Create login name: ")

    if createLogin in users:
        print ("\nLogin name already exist!\n")
    else:
        createPassw = input("Create password: ")
        users[createLogin] = createPassw
        print("\nUser created!\n")     

def signin():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    # check if user exists and login matches password
    if login in users and users[login] == passw: 
        print ("\nLogin successful!\n")
    else:
        print ("\nUser doesn't exist or wrong password!\n")

k=int(input('''
enter your choice:
1.sign in
2.sign up
3.exit '''))
if k==1:
    print(signin())
elif k==2:
    print(signup())
#while status!=q:
 #   displayMenu()
def withdraw():
    amt = int(input("enter amount: "))
    k= balance - amt
    print(k)
    
def deposit():
    amt = int(input("How much are you depositing? "))
    print('New balance: ',balance + amt)
def check():
    print('current balnce ',balance)
balance=0
choice = int(input('''
enter your choice::
1 - check balance
2 - withdraw
3 - deposit
4 - Exit:  '''))
if choice == 1:
    print(check())
elif choice == 2:
    print(withdraw())
elif choice == 3:
    print(deposit())
more=input('reenter the choice')

