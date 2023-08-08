def solution(s):
    answer = ''
    
    # words = list(s.split())
    # num_of_words = len(words)
    # for i, word in enumerate(words):
    #     if not word[0].isdigit() and word[0].islower():
    #         answer += word[0].upper() + word[1:].lower()
    #     else:
    #         answer += word
    #     if i != num_of_words - 1:
    #         answer += " "
    for i, v in enumerate(s):
        if v == ' ':
            answer += ' '
            continue
        if i == 0 or s[i - 1] == ' ':
            if not v.isdigit():
                answer += v.upper()
            else:
                answer += v
        else:
            answer += v.lower()
    return answer