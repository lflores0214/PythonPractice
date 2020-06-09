username = input("Enter your username")  # username
password = input("Enter your password")  # password


hidden_password = '*' * len(password)
password_length = len(password)
print(f'{username}, your password {hidden_password}, is {password_length} characters long')
