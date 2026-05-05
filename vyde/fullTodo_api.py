tasks = []

# Function to create Todo
def create_todo():
    title = input("Please enter the title : ")
    text = input("Please enter the ")

    task = {
        "title : ": title,
        "text : ": text
    }
    tasks.append(task)


# Function to update Todo
def update_todo():
    for i in range(1):
        create_todo()



# Function to delete Todo
# Function to store Todo

def main():
    update_todo()
    print()
