PATH = "tasks.txt"

def get_tasks():
    """
    Reads tasks from file and returns them as a list
    """
    with open(PATH, "r") as file:
        tasks_local = file.readlines()
    return tasks_local

def write_tasks(tasks_arg):
    """
    Writes/edits/removes tasks from file
    """
    with open(PATH, "w") as file:
        file.writelines(tasks_arg)

if __name__ == "__main__":
    print("Hello from functions")