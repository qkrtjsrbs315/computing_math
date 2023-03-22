def convert_money(n):
    obaek_won = n // 500
    n -= obaek_won*500
    baek_won = n // 100
    n -= baek_won*100
    oship_won = n // 50
    n -= oship_won*50
    ship_won = n // 10

    print("500원 동전의 개수:",obaek_won)
    print("100원 동전의 개수:",baek_won)
    print("50원 동전의 개수:",oship_won)
    print("10원 동전의 개수:",ship_won)



def get_integer():
    money = int(input('동전으로 교환하고자 하는 금액은?'))
    convert_money(money)

get_integer()