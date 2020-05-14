'''
Implementation for '/auth' routes

Authorisation:
Admin: Lecturer, Tutor

'''
from error import InputError
from helper_functions import is_email_valid
from helper_auth import is_email_valid, authenticate_user, log_user_in, log_user_out, \
    create_new_user, is_email_exist, check_access_error_token

def auth_login(email, password):
    '''Logging a user in'''
    does_email_exist, is_password_correct = authenticate_user(email, password)
    if not is_email_valid(email):
        raise InputError(f'{email} is not a valid email!')
    elif not does_email_exist:
        raise InputError('{email} doesn\'t exist, please try again!')

    elif not is_password_correct:
        raise InputError('Incorrect password, please try again!')
    else:
        u_id, token = log_user_in(email)
        return {
            'u_id': u_id,
            'token': token,
        }

def auth_logout(token):
    '''Logs user out'''
    check_access_error_token(token)
    is_success = log_user_out(token)
    return {'is_success': is_success,}

def auth_register(email, password, name_first, name_last):
    '''Registers a new user'''
    if not is_email_valid(email):
        raise InputError(f'{email} is not a valid email!')

    if is_email_exist(email):
        raise InputError('{email} already used, please try again!')

    if len(password) < 6:
        raise InputError('Password too short, please try again!')

    if len(name_first) not in range(1, 51):
        raise InputError('First name too short, please try again!')

    if len(name_last) not in range(1, 51):
        raise InputError('First name too short, please try again!')

    new_u_id, new_token = create_new_user(email, password, \
                                            name_first, name_last)
    return {
        'u_id': new_u_id,
        'token': new_token,
    }
