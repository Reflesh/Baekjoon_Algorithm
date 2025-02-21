#include <iostream>
using namespace std;
int n, m;
int arr[9];
bool visit[9];

void sol(int idx) {
    if(idx == m) {
        for(int i = 0; i < m; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
    } else {
        for(int i = 1; i <= n; i++) {
            if(!visit[i]) {
                visit[i] = true;
                arr[idx] = i;
                sol(idx + 1);
                visit[i] = false;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> m;
    sol(0);
    
    return 0;
}