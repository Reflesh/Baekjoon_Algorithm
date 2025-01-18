#include <iostream>
#include <vector>
using namespace std;

int main() {
    int num, v;
    int cnt = 0;
    cin >> num;

    vector<int> ls(num);
    for(int i = 0; i < num; i++) {
        cin >> ls[i];
    }

    cin >> v;

    for(int i = 0; i < num; i++) {
        if (ls[i] == v) {
            cnt++;
        }
    }

    cout << cnt << endl;
    
    return 0;

}