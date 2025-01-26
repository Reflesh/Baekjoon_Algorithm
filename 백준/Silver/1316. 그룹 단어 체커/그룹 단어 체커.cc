#include <iostream>
#include <string>
using namespace std;

bool isGroupWord(string word) {
    bool visited[26] = {false}; // 알파벳 출현 여부 확인
    char prev = word[0];        // 이전 index의 문자 저장
    visited[prev - 'a'] = true; // 첫 문자 방문 처리

    for (int i = 1; i < word.length(); i++) {
        char current = word[i];
        // 이전 문자와 다른 문자이고, 이미 등장한 문자라면 그룹 단어가 아님
        if (prev != current && visited[current - 'a']) {
            return false;
        }
        prev = current;
        visited[current - 'a'] = true;
    }
    return true;
}

int main() {
    int num;
    cin >> num;
    string word;
    int cnt = 0;

    for(int i = 0; i < num; i++) {
        cin >> word;
        if (isGroupWord(word)) {
            cnt++;
        }
    }

    cout << cnt << endl;
    return 0;
}