import re

def validate_passwords(input_string):
    passwords = input_string.split(',')
    valid_passwords = []

    for pwd in passwords:
        if len(pwd) < 6 or len(pwd) > 12:
            continue
        if not re.search("[a-z]", pwd):
            continue
        if not re.search("[A-Z]", pwd):
            continue
        if not re.search("[0-9]", pwd):
            continue
        if not re.search("[$#@]", pwd):
            continue
        valid_passwords.append(pwd)
    print(",".join(valid_passwords))
user_input = "ABd1234@1,a F1#,2w3E*,2We3345"
validate_passwords(user_input)