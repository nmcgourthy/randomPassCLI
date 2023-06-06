from functions.supabaseConfig import create_supabase_client
from functions.twilioSend import sendMessage
from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet

def getPasswords(user):
    print('sending sms to your phone ... ')
    validate = sendMessage(user.phoneNumber)
    if validate:
        supabase = create_supabase_client()
        table = supabase.table('passwords')
        response = table.select('password_name','encrypt_password').eq('email', user.email).execute()
            
        load_dotenv()
        key = os.getenv('ENCRYPTION_KEY')
        f = Fernet(key.encode('utf-8'))
        print('Passwords: ')
        for password in response.data:
            decrypted_password = f.decrypt(password['encrypt_password'].encode()).decode()
            print(password['password_name'] + ": " + decrypted_password)
            
        input('Press enter to continue ... ')
    else:
        print('Invalid sms')
