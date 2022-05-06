from credentails import User,Credentials


def create_new_user (username,password):
    """
    functtion to create new user
    """
    new_user = User(username,password)
    return new_user

def save_user (user):
    #save created user
    user.save_user()

def show_user():
    #display the saved user
    return User.display_user()

def login_user (username,password):
    #allow user to login
    check_user = Credentials.user_verification(username,password)
    return check_user

def create_new_credential(account,username,password):
    
    #create new credentials 
    new_credentials= Credentials(account,username,password)
    return new_credentials
    
def save_credentials(credentials):

    #save credentials to the credentials list
    credentials.save_datails()

def find_details(account):
    """
    find a credential from the credential list
    """
    return Credentials.find_credential(account)

def display_details ():
    #display saved credentials
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    delete a credentials from credentials list
    """
    credentials.delete_credentials()
