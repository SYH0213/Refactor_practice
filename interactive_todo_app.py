

class SimpleTodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task_name):
        self.tasks.append({'name': task_name, 'completed': False})
        print(f"-> 추가됨: '{task_name}'")

    def _find_task(self, task_name):
        for task in self.tasks:
            if task['name'] == task_name:
                return task
        return None

    def complete(self, task_name):
        task_to_complete = self._find_task(task_name)
        if task_to_complete:
            task_to_complete['completed'] = True
            print(f"-> 완료됨: '{task_name}'")
        else:
            print(f"-> 오류: '{task_name}' 항목을 찾을 수 없습니다.")

    def delete(self, task_name):
        task_to_delete = self._find_task(task_name)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            print(f"-> 삭제됨: '{task_name}'")
        else:
            print(f"-> 오류: '{task_name}' 항목을 찾을 수 없습니다.")

    def show(self):
        print("\n--- My To-Do List ---")
        if not self.tasks:
            print("할일이 없습니다!")
        else:
            for i, task in enumerate(self.tasks):
                status = '[x]' if task['completed'] else '[ ]'
                print(f"{i + 1}. {status} {task['name']}")
        print("---------------------")


def main():
    todo = SimpleTodoList()
    print("--- 인터랙티브 투두리스트 ---")
    print("명령어: add [할일], complete [할일], delete [할일], show, exit")

    while True:
        command_line = input("> ").strip()
        if not command_line:
            continue

        parts = command_line.split(' ', 1)
        command = parts[0]

        if command == 'add':
            if len(parts) > 1:
                todo.add(parts[1])
            else:
                print("-> 오류: 추가할 할일 내용을 입력하세요.")
        
        elif command == 'complete':
            if len(parts) > 1:
                todo.complete(parts[1])
            else:
                print("-> 오류: 완료할 할일 내용을 입력하세요.")

        elif command == 'delete':
            if len(parts) > 1:
                todo.delete(parts[1])
            else:
                print("-> 오류: 삭제할 할일 내용을 입력하세요.")

        elif command == 'show':
            todo.show()

        elif command == 'exit':
            print("프로그램을 종료합니다.")
            break
        
        else:
            print(f"-> 오류: 알 수 없는 명령어입니다: {command}")

if __name__ == "__main__":
    main()

