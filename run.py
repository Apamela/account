#!/usr/bin/env python3.6
def create_account(fname,user_name,password):
    '''
    Function to create a new account
    '''
    new_account = Account(fname,user_name,password)
    return new_account
def create_credential(fname,account_name,user_name,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(fname,account_name,user_name,password)
    return new_credential