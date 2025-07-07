
""" def process_data(data_list):
    even_numbers = []
    for item in data_list:
        if item % 2 == 0:
            even_numbers.append(item)

    squared_numbers = []
    for num in even_numbers:
        squared_numbers.append(num * num)

    total = 0
    for val in squared_numbers:
        total += val
    
    return total """


def process_data(data_list):
    return sum(num ** 2 for num in data_list if num % 2 == 0)

# 예시 데이터
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = process_data(my_list)
print(f"결과: {result}")
