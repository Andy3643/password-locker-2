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