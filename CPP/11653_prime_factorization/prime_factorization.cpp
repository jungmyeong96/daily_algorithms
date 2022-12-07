#include <iostream>

using namespace std;

int main()
{
    int num;

    cin >> num;
    while (num != 1)
    {
        for(int idx = 2; idx <= num; idx++)
        {
            if (num % idx == 0)
            {
                num = num / idx;
                cout << idx << endl;
                break;
            }
        }
    }
    return (0);
}