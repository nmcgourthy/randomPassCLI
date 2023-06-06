from functions.supabaseConfig import create_supabase_client
def checkUser():
    supabase = create_supabase_client()
    table = supabase.table('users')
    response = table.select('*').execute()
    if(response.data):
        return True
    else:
        print('no users found, create account')

        return False