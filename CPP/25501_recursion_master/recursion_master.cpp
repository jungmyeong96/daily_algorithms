#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int num_count = 0;

int recursion(const char* s, int l, int r) {
    num_count++;
    if (l >= r)
    {
        return 1;

    }
    else if (s[l] != s[r]) return 0;
    else
    {
        return recursion(s, l + 1, r - 1);
    }
}

int isPalindrome(const char* s) {
    return recursion(s, 0, strlen(s) - 1);
}

int main(){
    int word_num;
    cin >> word_num;

    for (int idx = 0; idx < word_num; idx++)
    {
        string word;
        cin >> word;

        cout << isPalindrome(word.c_str()) << " " << num_count << "\n"; //string으로 처리하면 처리속도가 느림
        num_count = 0;
    }
    return (0);
}