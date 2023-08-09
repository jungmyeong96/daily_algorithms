def solution(triangle):
    answer = 0
    checker = []
    for i, layer in enumerate(triangle):
        checker.append([])
        for j, element in enumerate(layer):
            if i != 0:
                if j == 0:
                    checker[i].append(element + checker[i - 1][j])
                elif j == len(layer) - 1:
                    checker[i].append(element + checker[i - 1][j - 1])
                else:
                    checker[i].append(max(element + checker[i - 1][j], element + checker[i - 1][j - 1]))
            else:
                checker[i].append(element)
    answer = max(checker[-1])
    return answer