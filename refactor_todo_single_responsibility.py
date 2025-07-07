

class SimpleTodoList:
    def __init__(self):
        # 각 할일은 딕셔너리 형태: {'name': '할일 이름', 'completed': False}
        self.tasks = []

    def add(self, task_name):
        # 새로운 할일을 추가
        self.tasks.append({'name': task_name, 'completed': False})
        print(f"추가됨: '{task_name}'")

    def _find_task(self, task_name):
        for task in self.tasks:
            if task['name'] == task_name:
                return task
        return None
            
    def complete(self, task_name):
        # 특정 할일을 완료 처리
        task_to_complete = self._find_task(task_name)
        if task_to_complete:
            task_to_complete['completed'] = True
            print(f"완료됨: '{task_name}'")
        else:
            print(f"오류: '{task_name}' 항목을 찾을 수 없습니다.")

    def delete(self, task_name):
        task_to_delete = self._find_task(task_name)
        if task_to_delete:
            self.tasks.remove(task_to_delete)
            print(f"삭제됨: {task_name}")
        else:
            print(f"오류: '{task_name}' 항목을 찾을 수 없습니다.")

    

    def show(self):
        # 전체 할일 목록을 보기 좋게 출력
        print("\n--- My To-Do List ---")
        if not self.tasks:
            print("할일이 없습니다!")
        else:
            for i, task in enumerate(self.tasks):
                if task['completed']:
                    status = '[x]'
                else:
                    status = '[ ]'
                print(f"{i + 1}. {status} {task['name']}")
        print("---------------------")


# 사용 예시
todo = SimpleTodoList()

todo.add("파이썬 공부하기")
todo.add("운동하기")
todo.show()

todo.complete("파이썬 공부하기")
todo.delete("운동하기")
todo.show()

todo.complete("장보기") # 없는 항목 완료 시도

