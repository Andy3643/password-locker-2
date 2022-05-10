
import unittest
from credentails import User


class TestUser(unittest.TestCase): 
    def setUp(self):
        """setup method that runs before each test case"""
        self.new_user = User("John Doe", "123456")
        User.user_list = []

    def test_init(self):
        #save user credentials
        self.assertEqual(self.new_user.account.username, "John Doe")
        self.assertEqual(self.new_user.account.password, "123456")


    def save_user (self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def tearDown(self):
      '''
      tearDown method that cleans up after each test case has run
      '''
      User.user_list = []

if __name__== '__main__':
    unittest.main()