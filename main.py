# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных
# задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description and not task.completed:
                task.mark_completed()
                return f"Task '{description}' Сделано."
        return f"Task '{description}' не найдено или завершено."

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            return "\n".join(f"{task.description} (Deadline: {task.deadline})" for task in current_tasks)
        return "No current tasks."

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2024-04-21")
task_manager.add_task("Посетить врача", "2024-04-22")
print(task_manager.list_current_tasks())
print(task_manager.mark_task_completed("Купить продукты"))
print(task_manager.list_current_tasks())

