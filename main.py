import json

from datetime import datetime

class file_modes:
    def file_read(self):
        with open(file_path, "r") as file:
            file_content = json.load(file)
            return file_content
    def file_write(self, content):
        self.content = content
        with open(file_path, "w") as file:
            json.dump(content, file, indent=4)

class Tasks(file_modes):

    def add_task(self):
        title = input("Enter your Task :").lower().strip().capitalize()
        status = input("Enter your Task Status:").lower().strip().capitalize()
        priority = input("Enter your Task Priority:").lower().strip().capitalize()
        due_date = input("Enter your Task Due Date:")

        content = {
            "title": title,
            "status": status,
            "priority": priority,
            "due_date": due_date
        }
        try:
            initial_file_content = super().file_read()
        except FileNotFoundError:
            initial_file_content = []
        initial_file_content.append(content)
        super().file_write(initial_file_content)
        print(f"The task {title} has been added!")
        del initial_file_content

    def delete_task(self):
        try:
            initial_file_content = super().file_read()

        except FileNotFoundError:
            print("There are no tasks!!")
        else:
            for task in initial_file_content:
                print(task["title"])
            print()
            del_task = input("Enter your Task to delete:").lower().strip().capitalize()
            for dict in initial_file_content:
                if del_task not in dict.values():
                    print(f"The task {del_task} not found!")
                    return
        
            for task in initial_file_content:
                if task["title"] == del_task:
                    initial_file_content.remove(task)

            super().file_write(initial_file_content)
            print(f"{del_task} has been deleted!")

    def view_tasks(self):
        try:
            file_content = super().file_read()
        except FileNotFoundError:
            print("No content found in the file")
        else:
            for task in file_content:
                for subtask in task:
                    print(f"{subtask} : {task[subtask]}")
                print()

    def mark_done(self):
        try:
            initial_file_content = super().file_read()
            for task in initial_file_content:
                print(task['title'])

        except FileNotFoundError:
            print("There are no tasks!!")

        else:
            task_done = input("Enter your Task to Mark Done:").lower().strip().capitalize()
            is_found = False
            for dict in initial_file_content:
                if task_done in dict.values():
                    is_found = True

            if is_found:
                for task in initial_file_content:
                    if task["title"] == task_done:
                        task["status"] = "Done"
                super().file_write(initial_file_content)
                print(f"{task_done} has been marked done!")

            else:
                print(f"{task_done} not in the file")


    def load_task(self):
        try:
            file_content = super().file_read()
            if file_content:
                for task in file_content:
                    if task['status'] == "Done" or task['status'] == "Completed":
                        continue
                    else:
                        for SubTask in task:
                            print(f"{SubTask}: {task[SubTask]}")
            else:
                print("There is no content in the file")
        except FileNotFoundError:
            print("There are no tasks!!")


    def edit_task(self):
        try:
            initial_file_content = super().file_read()
            for task in initial_file_content:
                print(task["title"])
            print()
            edit_task = input("Enter your Task to Edit:").strip()
        except FileNotFoundError:
            print("There are no tasks to edit!!")
            return
        is_found = False
        if initial_file_content:
            for task in initial_file_content:
                if task["title"] == edit_task:
                    is_found = True
                    print(task)
                    break
            if is_found:
                edit = input("Enter which task object to edit(title/status/due_date/priority):").lower().strip()
                if edit != "title" and edit != "status" and edit != "due_date" and edit != "priority":
                    print(f"The task {edit_task} does not exist!")
                else:
                    for i in range(len(initial_file_content)):
                        if edit_task in initial_file_content[i].values() and edit in initial_file_content[i].keys():
                            updated_value = input("Enter new value for " + edit + ":")
                            initial_file_content[i][edit] = updated_value
                    super().file_write(initial_file_content)
            else:
                print(f"{edit_task} not in the file")
        else:
            print(f"The file is empty!")

    def sort(self):
        print("1.By due date")
        print("2.By priority")
        print("3.By status")
        priority_dict = {
            "High":3,
            "Medium":2,
            "Low":1
        }
        status_dict = {
            "Pending": 3,
            "Incomplete": 2,
            "Completed": 1,
            "Done": 0
        }
        try:
            choice = int(input("Enter your choice(1-3):"))
            match(choice):
                case 1:
                    try:
                        initial_file_content = super().file_read()
                    except FileNotFoundError:
                        print("Theres no file to sort the data!!")
                    else:
                        for x in range(len(initial_file_content)):
                            initial_file_content[x]["due_date"] = datetime.strptime(initial_file_content[x]["due_date"], "%Y-%m-%d").date()
                            initial_file_content[x]["due_date"] = initial_file_content[x]["due_date"].strftime("%Y-%m-%d")
                            initial_file_content = sorted(initial_file_content , key = lambda x: x["due_date"])
                        super().file_write(initial_file_content)
                case 2:
                    try:
                        initial_file_content = super().file_read()
                    except FileNotFoundError:
                        print("There is no file to sort the data!!")
                    else:
                        if initial_file_content:
                            initial_file_content = sorted(initial_file_content , key = lambda x:priority_dict[x["priority"]] ,reverse= True)
                            super().file_write(initial_file_content)
                        else:
                            print("The file is empty!")
                case 3:
                    try:
                        initial_file_content = super().file_read()
                        if initial_file_content:
                            initial_file_content = sorted(initial_file_content , key = lambda x: status_dict[x["status"]] , reverse= True)
                            super().file_write(initial_file_content)
                        else:
                            print("There is no content in the file!!")
                    except FileNotFoundError:
                        print("There is no file to sort the data!!")
        except ValueError:
            print(f"Invalid choice!")

if __name__ == '__main__':
    global file_path
    file_path = "Tasks.json"
    task_manager = Tasks()


is_Running = True

while (is_Running):
    print("1.Add Task")
    print("2.Delete Task")
    print("3.View Tasks")
    print("4.Mark Done")
    print("5.Load Task")
    print("6.Edit Task")
    print("7.Sort")
    print("8.Exit")
    try:
        pointer = int(input("Enter your choice (1-8) :"))
    except ValueError:
        print(f"Invalid choice")
    else:
        match (pointer):
            case 1:
                task_manager.add_task()
            case 2:
                task_manager.delete_task()
            case 3:
                task_manager.view_tasks()
            case 4:
                task_manager.mark_done()
            case 5:
                task_manager.load_task()
            case 6:
                task_manager.edit_task()
            case 7:
                task_manager.sort()
            case 8:
                is_Running = False
                break

