#!/usr/bin/env python3.6
from account import Account#Importing the account class
from credential import Credential#Importing the credential class
def create_account(users_name,password):
    '''
    Function to create a new account
    '''
    new_account =Account(users_name,password)
    return new_account
def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()
def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()
def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()
def login_account(users_name,password):
   """
   login_account method to check a user and then sign in they exist
   """
   check_account = Account.login_account(users_name,password)
   return check_account
def create_credential(account_name,user_name,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account_name,user_name,password)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()
def del_credentials(credential):
    '''
    Function that to delete a credential 
    '''
    return Credential.delete_credentials()

def main():
    print("&"*80)
    while True:
              print("Use these short codes :\n cc - create a new account, \n dd - display accounts,\nlg- login your account")

              short_code = input().lower()

              if short_code == 'cc':
                      print("New Account")
                      print("#"*40)

                      print ("User name ....")
                      users_name = input()

                      print(" password ...")
                      password= input()
                      save_accounts(create_account(users_name,password)) # create and save new account.
                      print ('\n')
                      print(f"New Account {users_name} {password} created")
                      print ('\n')
                      
              elif short_code == 'dd':
                      print("#"40)
                           if display_accounts():
                                   print("Here is a list of all your accounts")
                                   print('\n')

                                   for account in display_accounts():
                                            print(f"Username:{account.users_name} \n Password:{account.password} ")

                                            print('\n')
                           else:
                            print('\n')
                            print("You dont seem to have any accounts saved yet")
                            print('\n')
              elif short_code=='lg':
                                 user_name1=input ("users_name:")
                                 
                                #  login=login_account(users_name,password)
                                 if user_name1!= users_name:
                                         continue
                                
                                 else:
                                     print()
                                     password1=input ("password:")
                                     if password1 !=password :
                                            continue
                                     else:
                                             pass

                                             while True:                
                                                print("Use these short codes : cc - create a new credential, dc - display credentials")

                                                short_code = input().lower()

                                                if short_code == 'cc':
                                                                print("New Credential")
                                                                print("-"*10)

                                                                print ("Account name ....")
                                                                account_name = input()

                                                                print("User name...")
                                                                user_name = input()

                                                                print("Password ...")
                                                                password = input()

                                                        

                                                                save_credentials(create_credential(account_name,user_name,password)) # create and save new credential.
                                                                print ('\n')
                                                                print(f"New Credential {account_name} {user_name} created")
                                                                print ('\n')

                                                elif short_code == 'dc':

                                                        if display_credentials():
                                                                print("Here is a list of all your credentials")
                                                                print('\n')

                                                                for credential in display_credentials():
                                                                    print(f"Account name:{credential.account_name}\n Username: {credential.user_name}\n Password:{credential.password}")
                                               
                                                else:
                                                                print('\n')
                                                                print("You dont seem to have any credentials saved yet")
                                                                print('\n')

                                       
                

                            
                    
if __name__ ==  '__main__':
    main()