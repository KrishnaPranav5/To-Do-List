import json


class Tasks:

    def add_task(self):
        title = input("Enter your Task :")
        status = input("Enter your Task Status:")
        priority = input("Enter your Task Priority:")
        due_date = input("Enter your Task Due Date:")
        content = {
            "title": title,
            "status": status,
            "priority": priority,
            "due_date": due_date
        }
        try:
            with open(file_path, "r") as file:
                initial_file_content = json.load(file)
        except FileNotFoundError:
            initial_file_content = []
        initial_file_content.append(content)
        with open(file_path, "w") as file:
            json.dump(initial_file_content, file, indent=4)
        del initial_file_content

    def delete_task(self, del_task):
        self.del_task = del_task
        initial_file = open(file_path, "r")
        initial_file_content = json.load(initial_file)
        initial_file.close()
        if del_task not in initial_file_content:
            print(f"{del_task} is not in the file!")
        else:
            for task in initial_file_content:
                if task["title"] == del_task:
                    initial_file_content.remove(task)
            with open(file_path, "w") as file:
                json.dump(initial_file_content, file, indent=4)


    def view_tasks(self):
        with open(file_path, "r") as file:
            file_content = json.load(file)
            for task in file_content:
                for subtask in task:
                    print(f"{subtask} : {task[subtask]}")
                print()

    def mark_done(self):
        task_done = input("Enter your Task to Mark Done:")
        file = open(file_path, "r")
        file_content = json.load(file)
        if task_done not in file_content:
            print(f"{task_done} is not in the file!")
        else:
            for task in file_content:
                if task["title"] == task_done:
                    task["status"] = "Done"
            file.close()
            with open(file_path, "w") as file:
                json.dump(file_content, file, indent=4)


    def load_task(self):
        file = open(file_path, "r")
        file_content = json.load(file)
        for task in file_content:
            for SubTask in task:
                if task["status"] != "Done":
                    print(f"{SubTask}: {task[SubTask]}")

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
    print("6.Exit")
    pointer = int(input("Enter your choice (1-6) :"))
    match pointer:
        case 1:
            task_manager.add_task()
        case 2:
            del_task = input("Enter your Task to delete:")
            task_manager.delete_task(del_task)
        case 3:
            task_manager.view_tasks()
        case 4:
            task_manager.mark_done()
        case 5:
            task_manager.load_task()
        case 6:
            is_Running = False
            break

