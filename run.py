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
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()
def main():
    print("Hello Welcome to your account list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
              print("Use these short codes : cc - create a new account, dc - display accounts, fc -find a account, ex -exit the account list ")

              short_code = input().lower()

              if short_code == 'cc':
                      print("New Account")
                      print("-"*10)

                      print ("User name ....")
                      users_name = input()

                      print(" password ...")
                      password= input()
                      save_accounts(create_account(users_name,password)) # create and save new account.
                      print ('\n')
                      print(f"New Account {users_name} created")
                      print ('\n')
              elif short_code == 'dc':

                           if display_accounts():
                                   print("Here is a list of all your accounts")
                                   print('\n')

                                   for account in display_accounts():
                                            print(f"{account.password}")

                                            print('\n')
                           else:
                            print('\n')
                            print("You dont seem to have any accounts saved yet")
                            print('\n')

# elif short_code == 'fc':

#     print("Enter the password you want to search for")

#     search_ = input()
#     if check_existing_accounts(search_password):
#         search_account = find_account(search_password)
#         print(f"{search_account.user_name} ")
#         print('-' * 20)

#      print(f"Password.......{search_account.password}")
#      print(f"Email address.......{search_account.user_name}")
#         else:
#          print("That account does not exist")

# elif short_code == "ex":
#     print("Bye .......")
#        break
#        else:
#     print("I really didn't get that. Please use the short codes")
def main():
    print("Hello Welcome to your credential list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list ")

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
                                            print(f"{credential.account_name} {credential.user_name} .....{credential.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

                    # elif short_code == 'fc':

                    #         print("Enter the name you want to search for")

                    #         search_number = input()
                    #         if check_existing_credentials(search_password):
                    #                 search_credential = find_credential(search_password)
                    #                 print(f"{search_credential.account_name} {search_credential.user_name}")
                    #                 print('-' * 20)

                    #                 print(f"User name.......{search_credential.credential_name}")
                    #                 print(f"Password.......{search_credential.password}")
                    #         else:
                    #                 print("That credential does not exist")

                    # elif short_code == "ex":
                    #         print("Bye .......")
                    #         break
                    # else:
                    #         print("I really didn't get that. Please use the short codes")
if __name__ ==  '__main__':
    main()