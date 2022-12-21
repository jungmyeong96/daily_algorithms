/*
    시간이 오버됨.
*/

// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int main()
// {
//     int count;
//     vector<int> arr;
//     vector<int>::iterator it;

//     cin >> count;
//     for (int tmp = 0; tmp < count; tmp++)
//     {
//         int num;
//         cin >> num;
//         arr.push_back(num);
//     }
//     sort(arr.begin(), arr.end());
//     for (int i = 0; i < count; i++)
//     {
//          cout << arr[i] << endl;
//     }
//     // for (it = arr.begin(); it != arr.end(); it++)
//     // {
//     //     cout << *it << endl;
//     // }
//     return (0);
// }

/*
    C와 C++의 stream동기화를 끊으면서 시간을 개선시킴
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    int arr[1000001];
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    sort(arr, arr + n);

    for (int i = 0; i < n; i++)
        cout << arr[i] << '\n';
    return(0);
}

//c 와 c++의 코드를 섞어쓸 수 없으니 참고할것