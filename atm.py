
from datetime import datetime
print(datetime.now())
username = input("Enter a username: \n")
database_username = {
   'Seyi':'passwordSeyi',
   'Mike':'passwordMike',
   'Love':'passwordLove'
}

def login():
    #login function here
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database_user and password == database_user[name]):
        print("Welcome " + name)
        return True
    else:
        print("Password or Username Incorrect. Please try again")
        return False
import re
def validate():
    while True:
        password = input("Enter a password: \n")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password seems fine")
            break
validate()

print("Welcome %s" % username )
print('These are the available options:')
print('1.Withdrawal')
print('2.Cash Deposit')
print('3.Complaint')

SelectedOption = int(input('Please select an option: \n'))
if SelectedOption is 1 :
    input('How much would you like to withdraw: \n')
    print('Take your cash')
    options = input("Do you want to go back to the available options ? Enter Y for yes or N for no \n")
if options.upper() == 'Y':
    print('These are the available options:')
    print('1.Withdrawal')
    print('2.Cash Deposit')
    print('3.Complaint')
    SelectedOption = int(input('Please select an option: \n'))
    
else:
    print('Thank you for using the ATM machine')

if SelectedOption is 2 :
    balance = input('How much would you like to deposit: \n') 
    print('Current Balance: %s' %balance)
    options = input("Do you want to go back to the available options ? Enter Y for yes or N for no \n")
if options.upper() == 'Y':
    print('These are the available options:')
    print('1.Withdrawal')
    print('2.Cash Deposit')
    print('3.Complaint')
    SelectedOption = int(input('Please select an option: \n'))
else:
    print('Thank you for using the ATM machine')
    
if SelectedOption is 3 :
    input('What issue would you like to report: \n')
    print('Thank you for contacting us')
    options = input("Do you want to go back to the available options ? Enter Y for yes or N for no \n")
if options.upper() == 'Y':
    print('These are the available options:')
    print('1.Withdrawal')
    print('2.Cash Deposit')
    print('3.Complaint')
    SelectedOption = int(input('Please select an option: \n'))
else:
    print('Thank you for using the ATM machine')
