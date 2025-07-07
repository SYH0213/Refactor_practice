

class StudentAnalyzer:
    def __init__(self, students_data):
        self.students = students_data

    def _error_data(self, student):
        iserror = False
        if len(student['scores']) != 0:
            for score in student['scores']:
                    if not isinstance(score, (int, float)):
                        iserror = True
        return iserror

    def _average_score(self, student):
        errordata = self._error_data(student)
        if not errordata:
            if len(student['scores']) != 0:
                return float(sum(student['scores']) / len(student['scores']))
        else:
            return None

    def analyze_grades(self):
        # 각 학생의 평균 점수를 계산하고 합격 여부를 판단
        analyzed_students = []

        for student in self.students:
            average = self._average_score(student)
            student['average'] = average
            if average != None:
                if self._average_score(student) >= 60:
                    student['passed'] = True
                else:
                    student['passed'] = False
                analyzed_students.append(student)
        return analyzed_students

    def generate_pass_report(self):
        # 합격한 학생들만 모아서 리포트 생성
        analyzed_data = self.analyze_grades()
        
        report_lines = []
        report_lines.append("--- 합격자 리포트 ---")
        
        for student_info in analyzed_data:
            if student_info['passed']:
                line = f"{student_info['name']}: 평균 {student_info['average']:.2f}점"
                report_lines.append(line)
        
        if len(report_lines) == 1: # 헤더만 있는 경우
            report_lines.append("합격자가 없습니다.")

        report_lines.append("---------------------")
        return "\n".join(report_lines)


# 예시 데이터
student_data = [
    {'name': '김철수', 'id': 'S001', 'scores': [85, 90, 78]},
    {'name': '이영희', 'id': 'S002', 'scores': [55, 60, 45]},
    {'name': '박지민', 'id': 'S003', 'scores': [70, 75, 80]},
    {'name': '최현우', 'id': 'S004', 'scores': [95, 92, 88]},
    {'name': '정미나', 'id': 'S005', 'scores': [30, 40, 50]},
    {'name': '오류학생', 'id': 'S006', 'scores': []}, # 점수가 없는 학생
    {'name': '이상한학생', 'id': 'S007', 'scores': ['a', 70, 80]}, # 잘못된 점수
]

# 분석 및 리포트 생성
analyzer = StudentAnalyzer(student_data)
report = analyzer.generate_pass_report()
print(report)

