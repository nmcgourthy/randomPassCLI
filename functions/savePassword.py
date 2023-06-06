import uuid

from functions import supabaseConfig


def savePassword(email, passwordName, encryptedPassword):
    supabase = supabaseConfig.create_supabase_client()
    
    try:
        response = supabase.table('passwords').insert({"id": str(uuid.uuid4()), "password_name": passwordName, "email": email, "encrypt_password": encryptedPassword}).execute()
        print('Password saved successfully')
    except Exception as e:
        print('Error saving password:', e)