import sys
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1 
#         for j <- i + 1 to n #n - 1 번, n - 2번, ... 1
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }
N = int(sys.stdin.readline())
sys.stdout.write(f'{(int)((N * (N - 1)) / 2)}\n2\n')

# n^2으로 수렴 
# 등차수열의 합 공식