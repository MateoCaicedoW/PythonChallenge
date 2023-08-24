class AuthenticationError(Exception):
    pass

def authenticate(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') == required_role:
                print(f"{required_role.capitalize()} authentication successful.")
                return func(user, *args, **kwargs)
            else:
                raise AuthenticationError(f"{required_role.capitalize()} authentication failed.")
        return wrapper
    return decorator

# Simulated user data with roles
users = [
    {'username': 'mateo', 'role': 'user'},
    {'username': 'astrid', 'role': 'admin'},
    {'username': 'caicedo', 'role': 'superuser'},
    {'username': 'caicedoError', 'role': ''},
]

def get_user_by_username(username):
    for user in users:
        if user['username'] == username:
            return user
    return None


def perform_actions(user):
    if user.get('role') == 'user':
        user_actions(user)
        print(f"Welcome, {user.get('username')}!")
    elif user.get('role') == 'admin':
        admin_actions(user)
        print(f"Welcome, {user.get('username')}!")
    elif user.get('role') == 'superuser':
        superuser_actions(user)
        print(f"Welcome, {user.get('username')}!")
    else:
        raise AuthenticationError("Authentication failed.")

@authenticate('user')
def user_actions(user):
    print("User actions accessed.")

@authenticate('admin')
def admin_actions(user):
    print("Admin actions accessed.")

@authenticate('superuser')
def superuser_actions(user):
    print("Superuser actions accessed.")

def main():
    try:
        username = input("Enter your username: ")
        user = get_user_by_username(username)
        
        if user:
            perform_actions(user)
        else:
            print("User not found.")
    except AuthenticationError as e:
        print(f"Authentication error: {e}")

if __name__ == "__main__":
    main()
