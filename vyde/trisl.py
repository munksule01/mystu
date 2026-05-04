def user_api():

    users = []

    for i in range(3):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")

        if len(password) < 4:
            print("Password must be at least 4 characters long.")
            continue

        user = {
            "username": username,
            "password": password
        }

        users.append(user)

    return users

data = user_api()

print(data)