class Account:
    """
    Class that generates new instances of accounts.
    """
    def __init__(self,user_name,password):

  # docstring removed for simplicitytring removed for simplicity

           self.user_name=user_name
           self.password=password
    account_list = [] # Empty account list
  # Init method up here
    def save_account(self):
        '''
        save_account method saves account objects into account_list
        '''
        Account.account_list.append(self)
@classmethod
def copy_user_name(cls,password):
        account_found = Account.find_by_password(password)
        pyperclip.copy(account_found.user_name)

