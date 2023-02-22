import sys
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
N = int(sys.stdin.readline())
sys.stdout.write(f'{(int)(((N) *(N - 1) *(N - 2)) / 6)}\n3\n')

# n^3으로 수렴 
# 등차수열의 합 공식

