# Mock user data
USER_DB = {
    'user1': {'authenticated': True},
    'user2': {'authenticated': False},
}


def authentication_required(fun):
    def wrapper(username, *args, **kwargs):
        user = USER_DB.get(username)
        if user and user['authenticated']:
            print(f"User {username} is authenticated.")
            return fun(username, *args, **kwargs)
        else:
            print(f'User {username} is not authenticated.Access Denied')
            return None

    return wrapper


@authentication_required
def access_sensitive_data(username, data_id):
    # Simulate accessing sensitive data
    return f'Sensitive Data {data_id} for User {username}'


# usage

access_sensitive_data('user1', 'data_123')  # Should Allow Access
access_sensitive_data('user2', 'data_456')  # Should Deny Access
