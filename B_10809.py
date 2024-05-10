# 단어에 포함되어 있는 경우 -> 처음 등장하는 위치 || 없을 시 -> -1

S = list(input())
list = [-1] * 26

for i in S:
    list[ord(i)-97] = S.index(i)

for i in list:
    print(i, end=' ')

'''
참고할 코드

s = input()
for i in range(97,123):
    print(s.find(chr(i)), end=' ')
'''