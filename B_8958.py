# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점

N = int(input())

for i in range(N):
    a = input()
    score = 0
    sumScore = 0

    for j in a:
        if j == 'O':
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)