# 10개 입력 후 42로 나눈 나머지 -> 서로 다른 값이 몇 개 있는지 출력

N_list = list(int(input()) for _ in range(10))
R_list = []

for i in N_list:
    R_list.append(i%42)

print(len(set(R_list)))

'''
다른 방법

arr = []

for i in range(10):
    N = int(input())
    if a%42 not in arr:
        arr.append(a % 42)
        
    print(len(arr))
'''