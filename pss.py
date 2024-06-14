def bypass_password(username):
    password=get_password_from_database(username)
    login(username,password)