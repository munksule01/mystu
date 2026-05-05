def todo_api():
    todos = []

    for todo in range(2):
        title = input("Enter title : ")
        text = input("Enter text : ")

        if text < 100:
            print("Text must be at least 100 characters long.")
            continue

        todo = {
            "Title : ": title,
            "text : " : text
        }

        todos.append(todo)

    return todos

data = todo_api();

print(data)