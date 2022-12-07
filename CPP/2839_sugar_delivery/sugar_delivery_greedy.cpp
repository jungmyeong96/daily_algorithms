#include <iostream>
using namespace std;

int N;
int main() {
    cin >> N;
    int ans = 0;
    //cout << 0 % 5 <<endl;// 0의 몫은 0
    while (N >= 0) {//마지막까지 3으로 나누어 떨어지지 않는다면 나눠지지 않는 값임.
        if (N % 5 == 0) {
            ans += N / 5;
            cout << ans << endl;
            return 0;
        }
        N -= 3;
        ans++;
    }
    cout << -1 << endl;
}