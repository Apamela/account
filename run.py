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
def create_credential(account_name,users_name,password):
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
    return Credentials.display_credentials()
   
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
    print("Hello Welcome to your contact list. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ ==  '__main__':
    main()