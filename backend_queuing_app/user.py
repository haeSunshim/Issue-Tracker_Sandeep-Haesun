'''
Implementation for '/user' routes
'''
from error import InputError
from data import get_data, update_data 
from helper_user import is_id_registered, is_name_valid, is_handle_valid,\
    same_email_exists, same_handle_exists
from helper_auth import generate_u_id, is_email_valid, is_token_valid

#@APP.route('/user/profile', methods=['GET'])
def user_profile(token, u_id):
    """return user info corresponding u_id"""
    if is_token_valid(token):
        data = get_data()
        if not is_id_registered(u_id):
            raise InputError
        for user in data['users_']:
            if u_id == user['u_id']:
                return {
                    'user': {
                        'u_id': user['u_id'],
                        'email': user['email'],
                        'name_first': user['name_first'],
                        'name_last': user['name_last'],
                        'handle_str': user['handle_str'],
                    },
                }
    return {}

def user_profile_setname(token, name_first, name_last):
    """update user name if it's valid"""
    if is_token_valid(token):
        data = get_data()
        if not is_name_valid(name_first)\
            or not is_name_valid(name_last):
            raise InputError
        for user in data['users_']:
            if token == user['token']:
                takeId = user['u_id']
                user['name_first'] = name_first
                user['name_last'] = name_last
                update_data(data)
    return {}

def user_profile_setemail(token, email):
    """update user email if it's valid"""
    if is_token_valid(token):
        data = get_data()
        if not is_email_valid(email):
            raise InputError
        if same_email_exists(email):
            raise InputError
        else:
            for user in data['users_']:
                if token == user['token']:
                    user['email'] = email
                    update_data(data)
    return {}

def user_profile_sethandle(token, handle_str):
    """update user handle if it's valid"""
    if is_token_valid(token):
        data = get_data()
        if not is_handle_valid(handle_str):
            raise InputError
        if same_handle_exists(handle_str):
            raise InputError
        for user in data['users_']:
            if token == user['token']:
                user['handle_str'] = handle_str
                update_data(data)
    return {}

