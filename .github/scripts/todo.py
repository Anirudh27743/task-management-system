
class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = status == "Done"
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        tasks = [
            Task("Complete assignment"),
            Task("Study Python"),
            Task("Prepare presentation"),
            Task("Review project", "Done"),
            Task("Complete testing", "Done"),
            Task("Update documentation", "Done")
        ]

        for task in tasks:
            self.add_task(task)

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


if __name__ == "__main__":
    task_pool = TaskPool()
    task_pool.populate()

    print("ToDo Tasks:")
    for task in task_pool.get_open_tasks():
        print(task.title)

    print("\nDone Tasks:")
    for task in task_pool.get_done_tasks():
        print(task.title)
