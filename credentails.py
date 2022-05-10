from venv import create
from requests import delete
import pyperclip
import random, string


class User:
    #list to store users
    user_list = []
    # create a class to store user credentials
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user (self):
        """
        method to save created user instance
        """
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user (self):
        """
        method to delete user
        """
        User.user_list.remove(self)

    @classmethod
    def user_verification (cls,username,password):
        #verify the user logins
        user_login = ""
        for user in User.user_list:
            if (User.username == username and User.password == password):
                user_login == user.username
                return user_login

class Credentials:
    credentials_list = []
    #create a class for user passwords to be stored
    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        #save user credentials
        Credentials.credentials_list.append(self)

    def delete_credentials (self):
        #delete user credentials
        Credentials.credentials_list.remove(self)

    
    @classmethod
    def find_credential(cls,account):
        #check if credential exist in the credentials list
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
            

    @classmethod
    def find_credential(cls,account):
        #check if credential exist in the credentials list
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return True
            else:
                 return False

    @classmethod
    def display_credentials (cls):
        return cls.credentials_list

    @classmethod
    def copy_credentials (cls,account):
        my_credential = Credentials.find_credential(account)
        pyperclip.copy(my_credential.password)


    def createPassword(stringLength=8):
        #create random  password for user
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(password) for i in range(stringLength))    
    


    