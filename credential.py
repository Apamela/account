class Credential:
    """
    Class that generates new instances of credentials
    """
    def __init__(self,user_name,password,account_name):

        # docstring removed for simplicitytring removed for simplicity

           self.password=password
           self.user_name=user_name
           self.account_name=account_name
    credential_list=[] # Empty credential list
  # Init method up here
    def save_credential(self):
        '''
        save_credential method saves credential objects into credential_list
        '''
        Credential.credential_list.append(self)





        