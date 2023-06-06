from functions.supabaseConfig import create_supabase_client

supabase = create_supabase_client()
table = supabase.table('passwords')
def deletePasswords(user):
    passwordName = input('What is the name of the password you want to delete?')
    response = table.select('password_name').eq('password_name', passwordName).eq('email',user.email).execute()
    if response:
        table.delete().eq('password_name', passwordName).execute()
        print('Password deleted')
    else:
        print('Password not found')

def updatePasswords(user):
    passwordName = input('What is the name of the password you want to change?')
    response = table.select('password_name').eq('password_name', passwordName).eq('email',user.email).execute()
    if response:
        print('What would you like to change ?')
        
        while True:
            print('1. Password name')
            print('2. Password')
            userInput = input()
            match userInput:
                case '1':
                    newPasswordName = input('What would you like the new name to be?')
                    table.update({'password_name': newPasswordName}).eq('password_name', passwordName).eq('email',user.email).execute()
                    print('Password name updated')
                    break
                case '2':
                    newPassword = input('What would you like the new password to be?')
                    confirm = input('confirm password')
                    if newPassword == confirm:
                        table.update({'password': newPassword}).eq('password_name', passwordName).eq('email', user.email).execute()
                        print('Password updated') 
                        break
                    else:
                        print('Passwords do not match')
                        continue
                case _:
                    print('Invalid choice')
                    continue
    else:
        print('Password not found')


def updatePassword(user):
    while True:
        print('1. Update password')
        print('2. Delete password')
        print('3. Go back')
        userInput = input('Enter your choice: ')
        match userInput:
            case '1':
                updatePasswords(user)
                break
            case '2':
                deletePasswords(user)
                break
            case _:
                print('Invalid choice')
                continue


