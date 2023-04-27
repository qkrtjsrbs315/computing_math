shopping_bag = []
shopping_count = {}
def append_things():
    while True:
        item = input('상품명? ')
        if item =="":
            print("장바구니 보기: ",shopping_bag)
            break
        else:
            cnt = int(input('수량은? '))
            shopping_bag.append(item)
            shopping_count[item] = cnt

def search_things():
    while True:
        item = input("장바구니에서 확인하고자 하는 상품은? ")
        if item =="":
            break
        else:
            print(f'{item}은(는) {shopping_count.get(item)}개 담겨 있습니다.')

append_things()
search_things()