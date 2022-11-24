#include <iostream>
// #include <vector>

using namespace std;

// bool checkId(vector<string> &ids, string answer)
// {
//     vector<string>::iterator ptr;
//     for (ptr = ids.begin(); ptr != ids.end(); ++ptr)
//     {
//         if (answer == *ptr)
//             return true;
//     }
//     ids.push_back(answer);
//     return false;
// }

// bool checkLower(string answer)
// {
//     for (int idx = 0; idx < answer.length(); ++idx)
//     {
//         if (!(answer[idx] >= 97 && answer[idx] <= 122))
//             return false;
//     }
//     return true;
// }

int main()
{
    string answer;
    // vector<string> ids;
    // while (1)
    // {
        cin >> answer;
        // if (checkLower(answer) && answer.length() <= 50)
        // {
            // if (checkId(ids, answer))
                cout << answer << "\?\?!" << std::endl;
            // else
            //     cout << answer << std::endl;
    //     }
    // }
    return 0;
}