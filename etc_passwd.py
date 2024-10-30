# Write a function, passwd_to_dict, that reads from a Unix-style “password file,” commonly stored as /etc/passwd, and returns a dict based on it.


# sample data
nobody: *: -2: -2: : 0: 0: Unprivileged User: / var/empty: / usr/bin/false
root: *: 0: 0: : 0: 0: System Administrator: / var/root: / bin/sh
daemon: *: 1: 1: : 0: 0: System Services: / var/root: / usr/bin/false


def passwd_to_dict():
    pass
