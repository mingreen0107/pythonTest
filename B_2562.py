# 9개의 서로 다른 자연수 -> 최댓값, 최댓값이 몇 번째 수

N_list = [int(input()) for _ in range(9)]

print(max(N_list))
print((N_list.index(max(N_list)))+1)