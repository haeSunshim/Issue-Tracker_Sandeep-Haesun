'''
Helper functions for '/auth' routes
'''
import hashlib
import random
from helper_functions import make_string
from data import get_data, update_data
from error import AccessError, InputError

import random
import string
import re

# # Returns a string of chosen length [1]
# def make_string(length):
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for i in range(length))

# Returns True/False if email is valid [2]
def is_email_valid(email):
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):  
        return True 
    else:  
        return False

def hashed(password):
    '''Encodes the password'''
    return hashlib.sha256(password.encode()).hexdigest()

def is_token_valid(token):
    '''Checks if token is valid'''
    data = get_data()
    for user in data['users_']:
        if token == user['token']:
            return True
    return False

def check_access_error_token(token):
    '''Error thrown when token passed in is not valid'''
    if not is_token_valid(token):
        raise AccessError('Invalid Token')

def generate_token():
    '''Generates token by hashing a random word'''
    word = make_string(random.randrange(100, 1000))
    new_token = hashed(word)

    #If token used by another user, then have to make another token
    while is_token_valid(new_token):
        # Very unlikely event, coverage likely won't cover this
        word = make_string(random.randrange(100, 1000))
        new_token = hashed(word)
    return new_token

def authenticate_user(email, password):
    '''Authenticates email/password combination'''
    data = get_data()
    for user in data['users_']:
        if email == user['email']:
            if hashed(password) == user['hash_password']:
                return (True, True)
            return (True, False)
    return (False, False)

def is_email_exist(email):
    '''Checks if email already exists'''
    data = get_data()
    for user in data['users_']:
        if email == user['email']:
            return True
    return False

def log_user_in(email):
    '''Logs user in and updates data base, assumes email is correct'''
    data = get_data()
    for user in data['users_']:
        if email == user['email']:
            user['is_active'] = True
            user['token'] = generate_token()

            update_data(data)
            return (user['u_id'], user['token'])
    # Very unlikely event, coverage likely won't cover this
    raise InputError('Incorrect email')

def log_user_out(token):
    '''Logs user out and updates database'''
    data = get_data()
    for user in data['users_']:
        if token == user['token'] and user['is_active']:
            user['is_active'] = False
            update_data(data)
            return True
    return False

def is_u_id_valid(u_id):
    '''Checks if u_id is valid'''
    data = get_data()
    for user in data['users_']:
        if u_id == user['u_id']:
            # Very unlikely event, coverage likely won't cover this
            return True
    return False

def generate_u_id():
    '''Generates id'''
    new_u_id = random.randrange(1000000000, 9999999999)

    #If u_id used by another user, generate another u_id
    while is_u_id_valid(new_u_id):
        # Very unlikely event, coverage likely won't cover this
        new_u_id = random.randrange(1000000000, 9999999999)
    return new_u_id

def is_handle_str_used(handle_str):
    '''Checks if u_id is valid'''
    data = get_data()
    for user in data['users_']:
        if handle_str == user['handle_str']:
            return True
    return False

def modify_handle_str(handle_str):
    '''If handle_str is used, generate a new one'''
    return handle_str[:15] + make_string(5)

def shorten_handle_str(handle_str):
    '''Shortens the handle_str if too long'''
    if len(handle_str) > 20:
        handle_str = handle_str[0:20]
    return handle_str

def generate_handle_str(name_first, name_last):
    '''Creates new handle_str'''
    handle_str = name_first.lower() + name_last.lower()
    handle_str = shorten_handle_str(handle_str)

    while is_handle_str_used(handle_str):
        handle_str = modify_handle_str(handle_str)
        handle_str = shorten_handle_str(handle_str)
    return handle_str

def generate_permission_id():
    '''If empty, make first user admin, otherwise not'''
    data = get_data()
    if not data['users_']:
        return 1
    return 2

def create_new_user(email, password, name_first, name_last):
    '''Creates a new user data structure'''
    data = get_data()

    new_user = {
        'u_id': generate_u_id(),
        'email': email,
        'name_first': name_first,
        'name_last': name_last,
        'handle_str': generate_handle_str(name_first, name_last),

        'permission_id': generate_permission_id(),
        'is_active': True,
        'token': generate_token(),
        'hash_password': hashed(password),
        'reset_code': hashed(password)[:10],
    }

    data['users_'].append(new_user)
    update_data(data)
    return (new_user['u_id'], new_user['token'])

#---------------------------------------------------------------------#
#                              References                             #
#---------------------------------------------------------------------#
'''
[1] Python, R. and Rogers, R. (2020). Random strings in Python. [online]
Stack Overflow. Available at: 
https://stackoverflow.com/questions/2030053/random-strings-in-python 
[Accessed 7 Mar. 2020].


[2]GeeksforGeeks. (2020). Check if email address valid or not in Python 
- GeeksforGeeks. [online] Available at: https://www.geeksforgeeks.org/
check-if-email-address-valid-or-not-in-python/ [Accessed 8 Mar. 2020].
'''
