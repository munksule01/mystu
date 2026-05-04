def user_api():

    users = []

    for i in range(3):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        user = {
            "username": username,
            "password": password
        }
        
        users.append(user)

    print(users)

user_api()