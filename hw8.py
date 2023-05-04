shopping_bag = {}
def append_things():
    print("[구입]")
    while True:
        item = input('상품명? ')
        if item == "":
            break
        count = int(input("수량은? "))
        shopping_bag[item] = count
        print(f'장바구니에 {item} {count}개가 담겼습니다.')


def search_things():
    while True:
        item = input("장바구니에서 확인하고자 하는 상품은? ")
        if item =="":
            break
        else:
            if shopping_bag.get(item) == None:
                print(f"장바구니에 {item}은(는) 없습니다.")
            else:
                print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')

append_things()
print(f'>>> 장바구니 보기: {shopping_bag}')
search_things()