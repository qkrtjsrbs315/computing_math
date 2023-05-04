# # # def input_list(lst):
# # #     name = input("이름? ")
# # #     num = input("번호? ")
# # #     lst.append(name)
# # #     lst.append(num)


# # # userinfo = []
# # # input_list(userinfo)
# # # print(f'{userinfo[1]}번 {userinfo[0]}')

# # def input_list():
# #     lst = []
# #     name = input("이름? ")
# #     num = input("번호? ")
# #     lst.append(name)
# #     lst.append(num)
# #     return lst

# # userinfo = input_list()
# # #input_list(userinfo)
# # print(f'{userinfo[1]}번 {userinfo[0]}')

# # def get_date():
# #     y = int(input("연도? "))
# #     m = int(input("월? "))
# #     d = int(input("일? "))
# #     return (y,m,d)

# # print("당신의 생일을 입력하세요: ")
# # bday = get_date()
# # print(f'당신의 만 60번째 생일은 {bday[0]+60}년 {bday[1]}월 {bday[2]}일 입니다.')


# def inspect_member():
#     members = []
#     for i in range(4):
#         a = int(input(str(i+1)+"층의 거주인원수는? "))
#         members.append(a)

#     return members
    


# def show_num_of_population(lst):
#     for i,member in enumerate(lst):
#         print(f'{i+1}층의 거주인원수는 {member}명입니다.')
    
    

# def get_total(lst):
#     total = 0
#     for n in lst:
#         total+=n
    
#     return total

# population = inspect_member()
# show_num_of_population(population)
# total = get_total(population)
# print(f'총 거주인원수는 {total}명 입니다.')

# scores = [["이찬수",95,85],["홍길동",90,80]]

# for i in scores:
#     for j in i:
#         print(j,end="/")
#     print()

# d = {
#     'python':'파이썬',
#     'basic':'기초',
#     'programming':'프로그래밍'
# }

# for key in d:
#     print(key)

# a = input().split()
# print(int(a[0])/int(a[1]))
#d = {'python':'파이썬'}

# def dict_get(dic,key):
#     if key in dic:
#         return dic[key]
#     else:
#         return None
# res = dict_get(d,'python')

# if res != None:
#     print(res)
# else:
#     print("오류: 잘못된 키")


#연습문제 10.2

# def find_max(ls):
#     max_value = ls[0]
#     for i in ls:
#         if i>max_value:
#             max_value = i
#     return max_value

# def append_ls():
#     num = []
#     for i in range(5):
#         num.append(int(input("정수 입력: ")))
#     return num
# nums = append_ls()
# max_num = find_max(nums)
# print(f'가장 큰 정수는 {max_num}입니다.')

#연습문제 10.3
# def get_average(ls):
#     sum = 0
#     for i in range(len(ls)):
#         sum+=ls[i]
#     return sum / len(ls)


# def input_scores():
#     a = []
#     for i in range(1,7):
#         score = int(input(f"#{i}?"))
#         if score > 0:
#             a.append(score)
#     return a

# def show_scores(ls):
#     print("[점수 출력]")
#     print("개인점수: ",end="")
#     for i in range(len(ls)):
#         print(ls[i],end=" ")
#     print()

# def search(ls):
#     while True:
#         num = int(input("찾고자 하는 점수는? "))
#         if num =="":
#             break
#         elif num not in ls:
#             print(f'{num}점을 받은 학생은 없습니다.')
#         elif num in ls:
#             for i in range(len(ls)):
#                 if num == ls[i]:
#                     print(f'{num}점은 학생은 {i+1}번 학생의 점수입니다.')




# ls = input_scores()
# ave = get_average(ls)
# show_scores(ls)
# print("평균:",ave)

# search(ls)