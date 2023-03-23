def get_fixed_price(p,d): #p는 할인된 가격 d는 할인율
    origin_price = p/(100-d)*0.1*1000 #80 * 8000 * 0.01
    print(origin_price)
    return origin_price

discount_ratio = int(input('할인율은? '))
a = int(input('A 상품의 할인된 가격은? '))
b = int(input('B 상품의 할인된 가격은? '))

a = get_fixed_price(a,discount_ratio)
b = get_fixed_price(b, discount_ratio)

print(f'A 상품의 정가는 {a} 원')
print(f'B 상품의 정가는 {b} 원')

