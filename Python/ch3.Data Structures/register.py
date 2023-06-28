def check_registration_rules(**users):
    valid_users=[]
    for username,password in users.items():
        if len(username)>=4 and len(password)>=6:
            if not (username=='quera' or username=='codecup'):
                if not password.isdigit():
                    valid_users.append(username)
    return valid_users