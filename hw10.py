from os import path
import pickle

FILENAME = "score.bin"
def load_data():
    with open(FILENAME,'rb') as file: 
        scores = pickle.load(file)
        sum = 0
        for i in scores:
            print(i, end=" ")
            sum += i
        avg = sum / len(scores)
        print("[점수출력]")
        print(f'평균점수:{avg}')    

def save_data(nums,avg):
    with open(FILENAME,'wb') as file:
        pickle.dump(nums,file)
        print("[점수출력]")
        for i in nums:
            print(i, end=" ")

        print(f'평균점수:{avg}')

def studentinfo():
    print("[점수입력]")
    i = 1
    nums = []
    sum = 0
    while True:
        n = int(input(f'#{i}?'))
        if n >=0:
            nums.append(n)
            sum+=n
            i+=1
        else:
            break
    avg = sum/len(nums)
    save_data(nums,avg)
 
if path.exists(FILENAME):
    load_data()
else:
    studentinfo()
    

