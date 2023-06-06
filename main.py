from user import User
from functions import savePassword, createUser,checkUser, createPassword, signIn, supabaseConfig, getPasswords, updatePasswords

supabaseConfig.create_supabase_client()

def promptAuth():
    print('Welcome to Password Manager: ')
    
    while True:
        print('1. sign in')
        print('2. sign up')
        userInput = input('Enter your choice: ')
        match userInput:
            case '1':
                valid, phoneNumber, name, email = signIn.signIn()
                if valid:
                    user = User(name, email, phoneNumber)
                    return user
            case '2':
                valid, email, phoneNumber, name = createUser.createCredentials()
                if valid:
                    user = User(name, email, phoneNumber)
                    return user
            case _:
                print('Invalid choice')
                continue

def promptAuthenticated(user):
    print('Welcome to Password Manager: ' + user.name)
    while True:
        print('1. create password')
        print('2. access passwords')
        print('3. update passwords')
        print('4. sign out')
        userInput = input('Enter your choice: ')
        match userInput:
            case '1':
                createPassword.createPassword(user.email)
            case '2':
                getPasswords.getPasswords(user)
            case '3':
                updatePasswords.updatePassword(user)
            case '4':
                user.logout()
                break
            case _:
                print('Invalid choice')
                continue
                
            
user = promptAuth()
promptAuthenticated(user)

# Last todo 
# 1. Add a function to delete a password
# 2. Account Help(recover password through sms)
