#include <iostream>
using namespace std;
int dp[5001]; //전역변수 선언을 통해 0으로 초기화

int main() {
    int n;
    cin >> n;
    //3kg 5kg를 혼합하여 최소봉지를 만들어야함
    dp[3] = dp[5] = 1; //최소봉지 초기화

    for (int idx = 6; idx <= n; idx++) //n의 값까지 반복을 돌며, 해당 값까지 도달하는 최소의 경우를 저장
    {
        if (dp[idx - 3]) dp[idx] = dp[idx - 3] + 1; //현재의 값에서 3을 뺀 값이 값이 있다면 현재의 값은 뺀 값 + 1
        if (dp[idx - 5]) dp[idx] = dp[idx] ? min(dp[idx], dp[idx - 5] + 1) : dp[idx - 5] + 1; //이미 3으로 나눴을 때와 값과 비교하여 더 작은 값이 있는지비교체크
    }
    cout << (dp[n] == 0 ? -1 : dp[n]) << endl; //0인경우 나눠질 수 없는 경우임.
    return 0;
}

