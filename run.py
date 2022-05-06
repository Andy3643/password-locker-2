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
