# Write a function, passwd_to_dict, that reads from a Unix-style “password file,” commonly stored as /etc/passwd, and returns a dict based on it.

# Each line is one user record, divided into colon-separated fields. The first field (index 0) is the username, and the third field (index 2) is the user’s unique ID number. (In the system from which I took the /etc/passwd file, nobody has ID -2, root has ID 0, and daemon has ID 1.) For our purposes, you can ignore all but these two fields.

# sample data:
# fake_passwd_file

def passwd_to_dict(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users


print(passwd_to_dict('fake_passwd_file'))
