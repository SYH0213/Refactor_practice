

class ReportGenerator:
    def __init__(self, user_data):
        self.users = user_data

    def create_report(self):
        """활성 사용자 리포트를 생성하여 반환합니다."""
        report_lines = self._get_formatted_lines()

        header = "--- ACTIVE USERS REPORT ---\n"
        footer = "\n--- END OF REPORT ---"
        return header + "\n".join(report_lines) + footer

    def _get_formatted_lines(self):
        """활성 사용자를 필터링하고 포맷팅하여 라인 리스트를 반환합니다."""
        return (f"USER: {u['name'].upper()}, EMAIL: {u['email']}"
                for u in self.users if u['is_active'])


# 예시 데이터
user_database = [
    {'name': 'Alice', 'email': 'alice@example.com', 'is_active': True},
    {'name': 'Bob', 'email': 'bob@example.com', 'is_active': False},
    {'name': 'Charlie', 'email': 'charlie@example.com', 'is_active': True},
    {'name': 'David', 'email': 'david@example.com', 'is_active': True},
]

# 리포트 생성 및 출력
report_builder = ReportGenerator(user_database)
report = report_builder.create_report()
print(report)

