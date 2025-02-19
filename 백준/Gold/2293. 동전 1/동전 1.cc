#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int num, coin;
    cin >> num >> coin;
    int cost[100];
    for(int i = 0; i < num; i++)
        cin >> cost[i];
    
    int dp[10001] = {0};
    dp[0] = 1;
    for(int i = 0; i < num; i++){
        for(int j = cost[i]; j < coin+1; j++) {
            dp[j] += dp[j-cost[i]];
        }
    }

    cout << dp[coin] << endl;
    
    return 0;
}