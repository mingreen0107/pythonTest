# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

N_list = [int(input()) for _ in range(9)]

print(max(N_list))
print((N_list.index(max(N_list)))+1)