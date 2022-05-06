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
  
    #find a credential from the credential list
  
    return Credentials.find_credential(account)

def display_details ():
    #display saved credentials
    return Credentials.display_credentials()

def copy_credentials(account):
  
    #A function that copies the credentials using the pyperclip
   
    return Credentials.copy_credentials(account)

def delete_credential(credentials):
 
    #delete a credentials from credentials list
    
    credentials.delete_credentials()

def generate_Password():
    #create a pasword for the user
    generated_new_password=Credentials.createPassword()
    return generated_new_password



#main function
def main():
    print("Welcome to Password Locker")
    print("*" *30)
    print("Choose short code to continue ;\nTo create an account, use create \nTo login to your account use login \nTo exit, type ex")
    short_code = input().lower().strip()
    print("\n")

    if short_code == "create":
        print ("Add a username")
        username = input("user_name")
        while True:
            print ("""choose to input your password, or let us genearate one for you.
            Type the following to make a choice:-
            input  ---to enter your password
            genpass  ---to let us generate a pasword for you""")
            user_input = input ().lower().strip()
            if user_input == "input":
                print("Enter your preffered password")
                password = input ()
                break
            elif user_input == "genpass":
                password = generate_Password()
                break
            else:
                print("Please enter a password to continue")





 if __name__ == '__main__':
    main()