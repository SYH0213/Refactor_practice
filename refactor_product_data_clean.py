""" 
def process_product_data(products):
    # 재고가 있고, 가격이 100달러 이상인 제품만 필터링
    valid_products = []
    for p in products:
        if p['stock'] > 0 and p['price'] >= 100:
            valid_products.append(p)

    # 제품명을 정리하고, 최종 문자열 생성
    result_list = []
    for p in valid_products:
        # 제품명 앞뒤 공백 제거 및 첫 글자 대문자화
        product_name = p['name'].strip()
        product_name = product_name.capitalize()
        
        # 최종 문자열 포맷팅
        info = f"{product_name} - ${p['price']}"
        result_list.append(info)

    return result_list """


def process_product_data(products):
    return [f"{p['name'].strip().capitalize()} - ${p['price']}" for p
             in products if p['stock'] > 0 and p['price'] >= 100]

    


# 예시 데이터
product_list = [
    {'name': '  laptop ', 'price': 1200, 'stock': 5},
    {'name': 'mouse', 'price': 25, 'stock': 10},
    {'name': ' monitor', 'price': 300, 'stock': 0},
    {'name': 'keyboard ', 'price': 150, 'stock': 8},
]

result = process_product_data(product_list)
print(result)
