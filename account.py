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