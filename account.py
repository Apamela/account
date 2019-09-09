class Account:
    """
    Class that generates new instances of accounts.
    """
    def __init__(self,users_name,password):

  # docstring removed for simplicitytring removed for simplicity

           self.users_name=users_name
           self.password=password
    account_list = [] # Empty account list
  # Init method up here
    def save_account(self):
        '''
        save_account method saves account objects into account_list
        '''
        Account.account_list.append(self)
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.account_list
        
    def login_account(users_name, password):
       """
       account_check_me method to check if a certain user is in user_list or not
       """
       check_me = ""
       for account in Account.account_list:
           if(account.users_name == users_name and account.password == password):
                check_me == account.users_name
       return check_me