#include <iostream>
using namespace std;


int checkGroup(string str)
{
    int alpha[26] = {};
    
    for (int idx = 0; idx < str.length(); idx++)
    {
        char checker = str[idx];
        int alphaIdx = checker - 'a';

        if (alpha[alphaIdx] == 1 && checker == str[idx - 1])
            continue;
        if (alpha[alphaIdx] == 0)
            alpha[alphaIdx] = 1;
        else
            return (0);
    }
    return (1);
}

int main()
{
    int count;
    int result;
    string tmp;

    cin >> count;
    result = 0;
    for (int idx = 0; idx < count; idx++)
    {
        tmp = "";
        cin >> tmp;
        result += checkGroup(tmp);
    }
    cout << result;
}