from functions import supabaseConfig
import bcrypt

def signIn():
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    supabase = supabaseConfig.create_supabase_client()
    table = supabase.table('users')
    response = table.select('hashPassword').eq('email', email).execute()

    if len(response.data) > 0:
        stored_hash = response.data[0]['hashPassword']
        encoded_password = password.encode('utf-8')
        userEncoded = stored_hash.encode('utf-8')

        if bcrypt.checkpw(encoded_password, userEncoded):
            print('Sign-in success')
            response = table.select('phoneNumber', 'name').eq('email', email).execute()
            phoneNumber = response.data[0]['phoneNumber']
            name = response.data[0]['name']
            del password, userEncoded
            return True, phoneNumber, name, email
        else:
            print('Incorrect password or email')
            return False, None, None, None
    else:
        print('User not found')
        return False, None, None, None