#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int M, N;
    scanf("%d %d", &M, &N);

    int arr[1000001] = {};

    for(int idx = 2; idx <= sqrt(N) + 1; idx++) //에라토스테네스의 체알고리즘
    {
        if (arr[idx] == 0){
            int jdx = 2;
            while (idx * jdx <= N)
            {
                arr[idx * jdx] = 1;
                jdx++;
            }
        }
    }
    for (int idx = M; idx <= N; idx++)
    {
        if (arr[idx] == 0)
                cout << idx << endl;
    }
}