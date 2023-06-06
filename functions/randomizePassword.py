# returns random password containing letters, numbers, and special characters

import random
import string

def generate_password():
    while True:
        try:
            while True:
                length = int(input('Password length: '))
                if length < 8:
                    print('Password must be at least 8 characters long.')
                    continue
                else:
                    break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        return password

