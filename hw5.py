def read_single_digit(one_number):
    if one_number == 48:
        return "영"
    elif one_number == 49:
        return "일"
    elif one_number == 50:
        return "이"
    elif one_number == 51:
        return "삼"
    elif one_number == 52:
        return "사"
    elif one_number == 53:
        return "오"
    elif one_number == 54:
        return "육"
    elif one_number == 55:
        return "칠"
    elif one_number == 56:
        return "팔"
    elif one_number == 57:
        return "구"

def read_number(num):
    result = ""
    for i in range(len(num)):
        result += read_single_digit(ord(num[i]))
    return result

   

while True:
    user_input = input("세 자리 정수 입력: ")
    if len(user_input) == 3:
        print(read_number(user_input))
        break
    elif len(user_input) == 2:
        user_input = "0"+user_input
        print(read_number(user_input))
        break
    elif len(user_input) == 1:
        user_input = "00"+user_input
        print(read_number(user_input))
        break

    else:
        print("다시 입력해주세요.")