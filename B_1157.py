# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램

word = input().upper()
word_list = list(set(word))
lst = []

for i in word_list:
    count = word.count(i)
    lst.append(count)

if lst.count(max(lst))>= 2:
    print("?")
else:
    print(word_list[lst.index(max(lst))])