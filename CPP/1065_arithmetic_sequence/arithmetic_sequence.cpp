#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool check_arith(int num)
{
    if (num == 1000)
        return false;
    if ((num / 100) - ((num / 10) % 10) == ((num / 10) % 10) - ((num % 10) / 1))
        return true;
    else
        return false;
}

int main()
{
    int count;
    int max;
    cin >> max;
    
    count = 0;
    for (int idx = 1; idx <= max; idx++)
    {
        if (idx <= 99)
        {
            count++;
            continue;
        }
        else if (check_arith(idx))
        {
            count++;
            continue;
        }
    }
    cout << count << endl;
    return (0);
}