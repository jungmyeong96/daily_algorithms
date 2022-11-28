#include <iostream>
using namespace std;

int main()
{
    int sum, count, price, ea, result;
    result = 0;
    cin >> sum >> count;
    while(count--)
    {
        cin >> price >> ea;
        result += price * ea;
    }
    if (result == sum)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    return (0);
}