import sys

dic, question = map(int,sys.stdin.readline().split())

dictionary = {}

for idx in range(dic):
    dictionary[idx + 1] = sys.stdin.readline().strip()

reverse_dictionary = {v:k for k,v in dictionary.items()}  #컴프리핸션을 통한 키밸류 변경

for _ in range(question):
    que = sys.stdin.readline().strip()
    if str.isdigit(que): #숫자체크
        print(dictionary[int(que)])
    else:
        print(reverse_dictionary[que])
