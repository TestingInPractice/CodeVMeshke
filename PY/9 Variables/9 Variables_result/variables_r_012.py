todos = []

def add_task(task, priority=3):
    todos.append({"task": task, "priority": priority})  # 1 — высший приоритет

def show_tasks():
    print("Список дел:")
    for idx, item in enumerate(todos, 1):
        print(f"{idx}. {item['task']} [Приоритет: {item['priority']}]")

add_task("Купить продукты", priority=1)
add_task("Позвонить другу")
show_tasks()
