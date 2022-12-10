#include <iostream>
using namespace std;

// struct arrset {
//     int num;
//     int col;
//     int row;
// };

// struct arrset arr[9][9] = {};

int main() 
{
    int col;
    int row;
    int max;
    int num;

    max = -1;
    for (int i = 1 ; i < 10 ; i++)
    {
        for (int j = 1; j < 10; j++)
        {
            cin >> num;
            if (num > max)
            {
                max = num;
                col = i;
                row = j;
            }
        }
    }
    cout << max << endl;
    cout << col << " " << row << endl;
    return (0);
}