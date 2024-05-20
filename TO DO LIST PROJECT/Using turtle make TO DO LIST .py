import turtle
import os

# Global variables
tasks = []
filename = "tasks.txt"
y_offset = 0

# Load tasks from a file
def load_tasks():
    global tasks
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.read().splitlines()

# Save tasks to a file
def save_tasks():
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display tasks
def display_tasks():
    turtle.clear()
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.write("To-Do List:", align="left", font=("Arial", 16, "bold"))
    for idx, task in enumerate(tasks, start=1):
        turtle.goto(-200, 200 - idx * 30)
        turtle.write(f"{idx}. {task}", align="left", font=("Arial", 14, "normal"))
    turtle.goto(-200, -100)
    turtle.write("Enter your command in the terminal and press 'Enter'.", align="left", font=("Arial", 12, "italic"))

# Function to add a task
def add_task():
    task = turtle.textinput("Add Task", "Enter the task:")
    if task:
        tasks.append(task)
        display_tasks()

# Function to remove a task
def remove_task():
    try:
        task_num = int(turtle.textinput("Remove Task", "Enter the task number to remove:"))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            display_tasks()
        else:
            turtle.textinput("Error", "Invalid task number. Press 'Enter' to continue.")
    except ValueError:
        turtle.textinput("Error", "Please enter a valid number. Press 'Enter' to continue.")

# Main function
def main():
    global y_offset
    load_tasks()
    turtle.speed(0)
    turtle.hideturtle()
    turtle.title("To-Do List App")
    display_tasks()

    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save and Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            save_tasks()
            print("Tasks saved. Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
