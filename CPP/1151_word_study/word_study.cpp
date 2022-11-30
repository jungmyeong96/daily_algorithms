#include <iostream>
#include <string>
#include <map>

using namespace std;


int main()
{
    string test;
    pair<char, int> result('?', 0);
    char alpha;
    map<char, int> counter;

    cin >> test;

    for (int i = 0; i < test.length(); i++)
    {
        if (islower(test[i]))
            alpha = toupper(test[i]);
        else
            alpha = test[i];
        map<char, int>::iterator iter = counter.find(alpha);
        if (iter != counter.end())
            counter[alpha] = counter[alpha] + 1;
        else
            counter[alpha] = 1;
    }
    for (map<char, int>::iterator iter = counter.begin(); iter != counter.end(); iter++)
    {
        if (iter->second > result.second)
        {
            result = *iter;
        }
        else if (iter->second == result.second)
        {
            result.first = '?';
        }
    }
    cout << result.first;
    return (0);
}