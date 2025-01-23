#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    int index;

    cin >> word;
    cin >> index;

    cout << word[index-1] << endl;

    return 0;

}