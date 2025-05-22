import re


def user_validator(user):
    errors = []
    if not (type(user[0]) == int and user[0]>0):
        errors.append('ID must be an integer > 0')

    if not (type(user[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user[1])):
        errors.append('user Name is Invalid')

    if not (type(user[2]) == str and re.match(r"^[a-zA-Z0-9]{3,30}$", user[2])):
        errors.append('Password is Invalid')

    if not (type(user[3]) == bool):
        errors.append('Status must be Active or Passive')

    if not (type(user[4]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user[4])):
        errors.append('Name is Invalid')

    if not (type(user[5]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user[5])):
        errors.append('Family is Invalid')

    return errors


