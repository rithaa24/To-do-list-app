import json

class Task:
    def __init__(self, title, description, status="To Do"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.description} - {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' deleted.")
                return
        print(f"Task '{title}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for task in self.tasks:
                print(task)

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            task_list = [{'title': task.title, 'description': task.description, 'status': task.status} for task in self.tasks]
            json.dump(task_list, file)
        print(f'Tasks saved to {filename}.')

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                task_list = json.load(file)
                self.tasks = [Task(task['title'], task['description'], task['status']) for task in task_list]
            print(f'Tasks loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found.')

# Testing the app
if __name__ == "__main__":
    todo_list = ToDoList()

    task1 = Task("Complete assignment", "Finish the programming assignment by Friday.")
    task2 = Task("Read a book", "Read 'The Hitchhiker's Guide to the Galaxy'.")
    task3 = Task("Exercise", "Go for a 30-minute run.")

    todo_list.add_task(task1)
    todo_list.add_task(task2)
    todo_list.add_task(task3)

    print("Initial task list:")
    todo_list.view_tasks()

    todo_list.delete_task("Read a book")
    
    print("\nTask list after deleting a task:")
    todo_list.view_tasks()

    todo_list.save_tasks("tasks.json")

    # Clearing the task list
    todo_list = ToDoList()

    # Loading tasks from the saved file
    todo_list.load_tasks("tasks.json")

    print("\nTask list after loading from file:")
    todo_list.view_tasks()
