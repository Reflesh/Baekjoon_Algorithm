#include <iostream>
#include <string>
using namespace std;

int main() {
    int alpha[26] = {0};
    int max_count = 0;
    char result = '?';

    string str;
    cin >> str; // 문자열 입력

    for (char c : str) {
        alpha[toupper(c) - 'A']++;
    }

    for (int i = 0; i < 26; i++) {
        if (alpha[i] > max_count) {
            max_count = alpha[i];
            result = 'A' + i;
        } else if (alpha[i] == max_count) {
            result = '?';
        }
    }

    cout << result << endl;

    return 0;
}