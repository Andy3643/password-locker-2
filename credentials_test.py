
import unittest
from credentails import Credentials


class TestCredentials(unittest.TestCase): 
    def setUp(self):
        """setup method that runs before each test case"""
        self.account = Credentials("facebook", "John Doe", "123456")
        Credentials.credentials_list = []

    def test_platform_created(self):
        #save user credentials
        self.assertEqual(self.account.account, "facebook")
        self.assertEqual(self.account.username, "John Doe")
        self.assertEqual(self.account.password, "123456")



if __name__== '__main__':
    unittest.main()