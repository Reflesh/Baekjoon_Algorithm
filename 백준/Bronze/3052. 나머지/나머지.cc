#include <iostream>
#include <vector>
using namespace std;

int main() {
    int num;
    int cnt = 0;
    vector<int> div(42, 0);
    for(int i = 0; i < 10; i++) {
        cin >> num;
        div[num % 42] = 1;
    }
    
    for(int i = 0; i < 42; i++) {
        if (div[i] == 1)
            cnt++;
    }

    cout << cnt << endl;

    return 0;

}