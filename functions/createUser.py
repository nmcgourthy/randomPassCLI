import re
import bcrypt
import uuid
import unittest
from functions import supabaseConfig

def createCredentials():
    supabase = supabaseConfig.create_supabase_client()
    passwordMatch = False
    # name
    while True:
        name = input('Name: ')
        choice = confirmChoice(name)
        if(choice):
            break
    # email
    while True:
        email = input('Email: ')
        choice = confirmChoice(email)
        if(not choice):
            continue
        if checkEmail(email):
            break
    # phone number
    while True:
        phoneNumber = input('Phone Number: ')
        choice = confirmChoice(phoneNumber[:3] + '-' + phoneNumber[3:6] + '-' + phoneNumber[6:])
        if(not choice):
            continue
        if checkPhone(phoneNumber):
            break
    # password
    while not passwordMatch:
        while True:
            password = input('Password: ')
            if passwordStrength(password):
                break
        while True:
            confirmPassword = input('Confirm Password: ')
            if confirmPassword == password:
                passwordMatch = True
                break
            else:
                print('Passwords do not match. Please try again.')
    # hash password
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    del password
    del confirmPassword

    # insert into database

    try:
        response_ = supabase.table('users').select('email').eq('email', email).execute()
        if len(response_.data) > 0:
            print('User already exists')
            return False,None, None, None
        else:
            data = supabase.table('users').insert({"id": str(uuid.uuid4()), "name": name, "email": email, "phoneNumber": phoneNumber, "hashPassword": hashedPassword.decode('utf-8')}).execute()
            print('User created successfully')
        
    except Exception as e:
        print('Error creating user:', e)
    return True, email, phoneNumber, name

    
def checkEmail(email):
    emailPattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.match(emailPattern, email.lower()):
        print('Valid Email')
        return True
    else:
        print('Invalid input. Please enter a valid email.')
        return False
    
def checkPhone(phoneNumber):
    phonePattern = r'^\d{10}$'
    if re.match(phonePattern, phoneNumber):
        print('Valid Phone Number')
        return True
    else:
        print('Invalid input. Please enter a valid phone number.')
        return False
    
def passwordStrength(password):
    # 8 characters
    if len(password) < 8:
        print('Password must be at least 8 characters long.')
        return False

    # uppercase 
    if not re.search(r'[A-Z]', password):
        print('1 uppercase letter required')
        return False

    # number 
    if not re.search(r'\d', password):
        print('1 number required')
        return False

    # special character
    if not re.search(r'[^A-Za-z0-9]', password):
        print('1 special character required')
        return False

    # If all conditions are met, the password is considered strong
    return True

def confirmChoice(value):
    while True:
        choice = input('confirm: ' + value + ' (y/n): ')
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Invalid input. Please enter y or n.')