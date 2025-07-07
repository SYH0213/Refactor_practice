

class StudentAnalyzer:
    def __init__(self, students_data):
        self.students = students_data

    def _calculate_average(self, scores):
        """점수 리스트를 받아 평균을 계산하고, 오류 발생 시 None을 반환합니다."""
        if not scores: # 점수 리스트가 비어있는 경우
            return None
        try:
            # 모든 점수가 숫자인지 확인하며 합계 계산
            total_score = sum(score for score in scores if isinstance(score, (int, float)))
            # 만약 숫자가 아닌 값이 섞여있다면 sum()에서 TypeError가 발생할 수 있음
            # 또는, 모든 요소가 숫자가 아닐 경우 total_score가 0이 될 수 있으므로 len()으로 다시 확인
            
            # 유효한 점수만 필터링하여 평균 계산
            valid_scores = [score for score in scores if isinstance(score, (int, float))]
            if not valid_scores: # 유효한 점수가 하나도 없는 경우
                return None

            return float(total_score / len(valid_scores))
        except TypeError: # 점수 중에 숫자가 아닌 것이 섞여있을 때
            return None
        except Exception: # 그 외 예상치 못한 오류
            return None

    def analyze_grades(self):
        """각 학생의 평균 점수를 계산하고 합격 여부를 판단하여 새로운 리스트를 반환합니다."""
        analyzed_students = []
        for student in self.students:
            average = self._calculate_average(student['scores'])
            
            # 분석된 학생 정보를 담을 새로운 딕셔너리 생성
            analyzed_info = {
                'name': student['name'],
                'id': student['id'], # ID도 함께 포함
                'average': average, # None일 수도 있음
                'passed': False # 기본값
            }

            if average is not None: # 평균이 유효한 경우에만 합격 여부 판단
                if average >= 60:
                    analyzed_info['passed'] = True
                # else: passed는 이미 False로 초기화되어 있음
                analyzed_students.append(analyzed_info)
            # else: average가 None인 학생은 analyzed_students에 추가하지 않음

        return analyzed_students

    def generate_pass_report(self):
        """합격한 학생들만 모아서 리포트 문자열을 생성합니다."""
        analyzed_data = self.analyze_grades()
        
        report_lines = []
        report_lines.append("--- 합격자 리포트 ---")
        
        found_passer = False
        for student_info in analyzed_data:
            if student_info['passed']:
                line = f"{student_info['name']}: 평균 {student_info['average']:.2f}점"
                report_lines.append(line)
                found_passer = True
        
        if not found_passer: # 합격자가 한 명도 없는 경우
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
    {'name': '또다른오류', 'id': 'S008', 'scores': ['b', 'c']}, # 모두 잘못된 점수
    {'name': '점수만점', 'id': 'S009', 'scores': [100, 100, 100.0]}, # float 점수 포함
]

# 분석 및 리포트 생성
analyzer = StudentAnalyzer(student_data)
report = analyzer.generate_pass_report()
print(report)

