# c d e f g a b C -> c는 1로, d는 2로, ..., C를 8로 바꾼다.

a = list(map(int, input().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')

'''
내가 쓴 코드 성장해라 송민쥬

list = input().split()
cntp = 0
cntm = 0
j = 1
k = 8

for i in list:
    i = int(i)
    if (i == j):
        cntp += 1
        j += 1
    if (i == k):
        cntm += 1
        k -= 1

if (cntp == 8):
    print("ascending")
elif (cntm == 8):
    print("descending")
else:
    print("mixed")
'''