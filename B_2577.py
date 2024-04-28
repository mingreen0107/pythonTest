# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

N = [int(input()) for _ in range(3)]
number_list = []
result = 1

for i in range(3):
    result *= N[i]
for i in range(1, 10):
    number_list[i] = 0
result_list = list(map(int, str(result)))
for i in result_list:
    i = int(i)
    number_list[i] += 1