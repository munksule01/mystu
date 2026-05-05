tasks = []

# Function to create Todo
def create_todo():
    title = input("Please enter the title : ")
    description = input("Please enter the description : ")

    if description == "":
        print("Description cannot be empty.")
        return

    task = {
        "title:": title,
        "description:": description
    }
    tasks.append(task)

    print("Todo created successfully.")


# Function to update Todo
def update_todo():
    title = input("Please enter the title of the Todo to update : ")
    new_description = input("Please enter the new description : ")

    for task in tasks:
        if task["title:"] == title:
            task["description:"] = new_description
            print("Todo updated successfully.")
            return

    print("Todo not found.")


# Function to delete Todo
def delete_todo():
    title = input("Please enter the title of the Todo to delete : ")

    for task in tasks:
        if task["title:"] == title:
            tasks.remove(task)
            print("Todo deleted successfully.")
            return

    print("Todo not found.")

# Function to store Todo

def store_todo():
    with open("todos.txt", "w") as file:
        for task in tasks:
            file.write(f"Title: {task['title:']}\n")
            file.write(f"Description: {task['description:']}\n")
            file.write("\n")

    print("Todos stored successfully.")

# Function to display all Todos
def display_todos():
    if not tasks:
        print("No Todos to display.")
        return

    for task in tasks:
        print(f"Title: {task['title:']}")
        print(f"Description: {task['description:']}")
        print("\n")

# Main function to run the Todo API
def main():
    while True:
        print("1. Create Todo")
        print("2. Update Todo")
        print("3. Delete Todo")
        print("4. Store Todos")
        print("5. Display Todos")
        print("6. Exit")

        choice = input("Please select an option : ")

        if choice == "1":
            create_todo()
        elif choice == "2":
            update_todo()
        elif choice == "3":
            delete_todo()
        elif choice == "4":
            store_todo()
        elif choice == "5":
            display_todos()
        elif choice == "6":
            print("Exiting the Todo API.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()