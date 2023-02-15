import sys

word1 = sys.stdin.readline().strip()
word2 = sys.stdin.readline().strip()

w_len1 = len(word1)
w_len2 = len(word2)

buf = [0] * w_len1


#cnt를 누적 변수로 사용하고, 누적 변수의 값이 버퍼값보다 작으면 교체
#글자가 같은 경우에 누적 변수에서 1을 더한다.
for i in range(w_len2):
    cnt = 0
    for j in range(w_len1):
        # if word1[j] == word2[i] and buf[j] < max(word1):
        #     buf[i] = max(buf[i], buf[j] + 1)
        if cnt < buf[j]: #
            cnt = buf[j]
        elif word1[j] == word2[i]:
            buf[j] = cnt + 1
    
sys.stdout.write("%d\n" % max(buf))