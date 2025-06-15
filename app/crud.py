todos = []
id_counter = 1

def get_todos():
    return todos

def add_todo(task):
    global id_counter
    todos.append({"id": id_counter, "task": task})
    id_counter += 1

def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
