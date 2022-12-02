#include <iostream>
#include <string>

using namespace std;


void calcBigNum(int bigLen, int smallLen, string big, string small)
{
    int sum;
    int jdx = smallLen;
    int upper = 0;
    string ans = "";
    for (int idx = bigLen - 1; idx >= 0; idx--)
    {
        jdx--;
        if (jdx >= 0)
            sum = (big[idx] - '0') + (small[jdx] - '0') + upper;
        else
            sum = (big[idx] - '0') + upper;
        if (sum >= 10) {
            ans.insert(0, to_string(sum % 10));
            upper = 1;
        }
        else{
            ans.insert(0, to_string(sum));
            upper = 0;
        }
    }
    if (upper == 1)
        ans.insert(0, to_string(upper));
    // int front_not_zero = ans.find_first_not_of('0');
    // ans.erase(0, front_not_zero);
    // if (ans == "")
    //     ans.insert(0, "0");
    cout << ans;
}

int main()
{
    string a;
    string b;
    cin >> a >> b;

    int aLen = a.length();
    int bLen = b.length();
    int sLen;
    if (aLen >= bLen)
        calcBigNum(aLen, bLen, a, b);
    else
        calcBigNum(bLen, aLen, b, a);

    return (0);
}