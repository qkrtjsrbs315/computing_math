def draw_line_string(user_input):
    msg1 = "Hello "+user_input #유저 입력 
    msg2 = "Welcome to Seoul"
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

    print("-"*nstr)
    print(msg1 + ",")
    print(msg2 + ".")
    print("-"*nstr)


user_i = input("Input his/her name: ")
draw_line_string(user_i)