def user_api():

    users = []
    user = []

    for i in range(3):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")    
        user.append(username)
        user.append(password)
        users.append(user)
        user = []  # Reset the user list for the next iteration
        
    print(users)

user_api()
