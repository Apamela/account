import pyperclip
import unittest#Importing the unittest module
from account import Account#Importing the account class
from credential import Credential#Importing the credential class
class TestAccount(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviors.
    Args:
         unittest.TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("polla","polla12") # create account object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.users_name,"polla")
        self.assertEqual(self.new_account.password,"polla12")
    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
        the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviors.
    Args:
         unittest.TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("pamelous","pampam12","poela12") # create credential object
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"pamelous")
        self.assertEqual(self.new_credential.password,"pampam12")
        self.assertEqual(self.new_credential.account_name,"poela12")
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
        the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)
def test_copy_user_name(self):
        '''
        Test to confirm that we are copying the user_name address from a found account
        '''

        self.new_account.save_account()
        Account.test_copy_users_name("polla12")

        self.assertEqual(self.new_account.users_name,pyperclip.paste())


def test_copy_credential_name(self):
        '''
        Test to confirm that we are copying the account_name address from a found credential
        '''

        self.new_credential.save_credential()
        Credential.test_copy_account_name("pampam12")

        self.assertEqual(self.new_credential.account_name,pyperclip.paste())

# @classmethod
# def copy_user_name(cls,password):
#         account_found = Account.find_by_password(password)
#         pyperclip.copy(account_found.user_name)








if __name__ == '__main__':
    unittest.main()
