'''
Helper functions for user.py
'''
from data import get_data
def is_id_registered(u_id):
    """check if u_id is valid"""
    data = get_data()
    for user in data['users_']:
        if u_id == user['u_id']:
            return True
    return False

def is_name_valid(name):
    """return True if name is between 1 and 50 characters inclusive in length"""
    if 1 <= len(name) <= 50:
        return True
    return False

def same_handle_exists(given_handle):
    """check if any handle string duplicates"""
    data = get_data()
    for user in data['users_']:
        if given_handle == user['handle_str']:
            return True
    return False

def is_handle_valid(handle_str):
    """
return False if NOT handle_str between 2 and 20 characters inclusive
    """
    if len(handle_str) not in range(3, 21):
        return False
    return True

def same_email_exists(email):
    """check if the email user trying to update already exists"""
    data = get_data()
    for user in data['users_']:
        if email == user['email']:
            return True
    return False
