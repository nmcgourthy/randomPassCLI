from functions import randomizePassword, savePassword

from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

CONFIRM_PASSWORD_NAME = 'y'
RENAME_PASSWORD = 'n'

# encrypt password
def encryptPassword(password):
    load_dotenv()
    key = os.getenv('ENCRYPTION_KEY')
    f = Fernet(key.encode('utf-8'))
    encryptedPassword = f.encrypt(password.encode('utf-8'))

    del password
    return encryptedPassword

def createPassword(email):
    while True:
        passwordName = input('What is the name of the password?')
        userInput = input('confirm password name: ' + passwordName + ' (y/n)')
        userInput = userInput.lower()
    
        if(userInput == CONFIRM_PASSWORD_NAME):
            break

        elif(userInput == RENAME_PASSWORD):
            continue
        else:
            print('Invalid input. Please enter y or n.')
            continue
    while True:
        print('Password:')
        print('1. Generate strong password')
        print('2. Enter your own password')
        userInput = input('Enter your choice: ')
        match userInput:
            case '1':
                password = randomizePassword.generate_password()
                print('Your strong password is: ' + password)
                break
            case '2':
                password = input('Enter your password: ')
                break
            case _:
                print('Invalid choice')
                continue

    encryptedPassword = encryptPassword(password)
    savePassword.savePassword(email , passwordName, encryptedPassword.decode('utf-8'))

    # clear variables because data leak bad !!
    del passwordName
    del password




    


