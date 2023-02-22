import sys
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }
N = int(sys.stdin.readline())
sys.stdout.write(f'{N * N * N}\n3\n')

# n^3으로 수렴 