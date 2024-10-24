'''
TO-DO List App

We are building a simple console-based To-Do List application where users can
ADD, UPDATE & DELETE Tasks.

here, we can store tasks in a text file (or) by using a simple JSON file for practice

'''
import time

#Create a To Do list class
class ToDoList:
    #initialising a constutor function
    def __init__(self):
        #making an empty list so we can save all the task we add later
        self.tasks = []
    
    #function for add new task into the To Do List
    def add_task(self, title, description):
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        task = {"title": title, "description": description, "date": date}
        #adding the task into the "tasks" empty list
        self.tasks.append(task)
        print(f'\nTask {title} added successfully!')

    #function for viewing all the task in out to do list
    def view_tasks(self):
        print("\n ----WELCOME TO YOUR TO-DO LIST----")
        #option is there are No tasks in the list
        if not self.tasks:
            print("\nNo tasks available in your To-Do List")
        else:
            #assigning index to all the actions by enumeration
            print("\nYour TO-DO List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f'\nTask {index}:')
                print(f' Title           : {task['title']}')
                print(f' Description     : {task['description']}')
                print(f' Added on        : {task['date']}')

    #funtion for changing already existing list
    def update_task(self, index):
        #for index = 0 or greater than length of "tasks" list
        if index < 1 or index > len(self.tasks):
            print("\nInvalid task number!")
            return
        
        new_title = input("\nEnter new title: ")
        new_description = input("Enter new description: ")
        self.tasks[index - 1]["title"] = new_title
        self.tasks[index - 1]["description"] = new_description
        print(f"\nTask {index} updated successfully!")

    #function for deleting existing task
    def delete_task(self, index):
        #for index = 0 or greater than length of "tasks" list
        if index < 1 or index > len(self.tasks):
            print("\nInvalid task number!")
            return
        
        #using a simple pop funtion to remove the task in "tasks" list
        removed_task = self.tasks.pop(index - 1)
        print(f'\nTask "{removed_task['title']}" deleted successfully')

    #Interaction Palate, how users can interact with the TO DO list
    def main_menu(self):
        while True:
            print("\n ---- TO DO List Menu ----")
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == "1":
                title = input("\nEnter Task Title: ")
                description = input("Enter Task Description: ")
                self.add_task(title, description)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                try:
                    index = int(input("\nEnter Task Number to Update: "))
                    self.update_task(index)
                except ValueError:
                    print("\nPlease enter a valid task number!")
            elif choice == "4":
                try:
                    index = int(input("\nEnter the task number you want to Delete: "))
                    self.delete_task(index)
                except ValueError:
                    print("\nPlease enter a valid task number!")
            elif choice == "5":
                print("\nExiting To-Do List App. GoodBye!")
                break
            else:
                print("\nInvalid Choice Number! Please select a valid option.")

#printing the whole To Do list App
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.main_menu()
        

