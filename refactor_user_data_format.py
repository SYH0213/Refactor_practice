""" 
def process_user_data(user_list):
    # 활성 상태인 사용자만 필터링
    active_users = []
    for user in user_list:
        if user["is_active"] == True:
            active_users.append(user)

    # 결과 문자열 포맷팅
    formatted_strings = []
    for user in active_users:
        info = "User " + user["name"] + " (id: " + str(user["id"]) + ")" 
        formatted_strings.append(info.upper())
    
    return formatted_strings
 """
def process_user_data(user_list):
    return [f"User {user['name']} (id: {user['id']})".upper() for user in user_list if user['is_active']]

# 예시 데이터
users = [
    {"id": 1, "name": "alice", "is_active": True},
    {"id": 2, "name": "bob", "is_active": False},
    {"id": 3, "name": "charlie", "is_active": True},
]

result = process_user_data(users)
print(result)
