USERS = [
    {
        "id": 0,
        "username": "test",
        "password": "test",
        "email": "test@gmail.com"
    }
]

def compare_user_password(user_model, password):
    result = False
    if(user_model['password'] == password):
        result = True
    return result
    


def get_user_by_email(email):
    for user in USERS:
        if user['email'] ==email:
            return user
    return None

def create_user(username, password, email):
    new_user = {
        "id": len(USERS),
        "username": username,
        "password": password,
        "email": email
        }
    USERS.append(new_user)
    return new_user


def get_all_user():
    return USERS