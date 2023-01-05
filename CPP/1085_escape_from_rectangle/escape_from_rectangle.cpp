#include <iostream>
using namespace std;

int main()
{
    int x, y, w, h;
    cin >> x >> y >> w >> h;

    int x_min = w - x > x - 0 ? x - 0 : w - x;
    int y_min = h - y > y - 0 ? y - 0 : h - y;
    if (x_min < y_min)
        cout << x_min;
    else
        cout << y_min;
    return (0);
}