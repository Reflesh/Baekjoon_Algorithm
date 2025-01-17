#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> basket(n);

    for(int i = 0; i < n; i++) {
        basket[i] = i + 1;
    }

    for(int i = 0; i < m; i++) {
        int f, s;
        cin >> f >> s;
        swap(basket[f-1], basket[s-1]);
    }

    for(int i = 0; i < n; i++) {
        cout << basket[i] << " ";
    }
    cout << endl;
    
    return 0;

}