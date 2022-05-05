from requests import delete
import pyperclip


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