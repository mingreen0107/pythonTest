# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성

N = int(input())

for i in range(1, 10):
    i = int(i)
    print(N, "*", i, "=", N*i)