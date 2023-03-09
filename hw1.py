def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area(r):
    s = r*r*3.14
    return s
 
circle_r = get_radius('넓이를 구하고자 하는 원의 반지름은?') #원의 반지름

circle_s = get_circle_area(circle_r) #원의 넓이

print(f'반지름 {circle_r}인 원의 넓이 = 3.14 x {circle_r} x {circle_r} = {circle_s}')