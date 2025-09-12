#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int caseCount;
    cin >> caseCount;

    while(caseCount) {
        int sticker_num;
        cin >> sticker_num;

        vector<vector<int>> sticker(2, vector<int>(sticker_num));
        for (int i=0; i<2; i++) {
            for (int j=0; j<sticker_num; j++) {
                cin >> sticker[i][j];
            }
        }

        vector<vector<int>> dp(2, vector<int>(sticker_num));
        dp[0][0] = sticker[0][0];
        dp[1][0] = sticker[1][0];

        if(sticker_num > 1) {
            dp[0][1] = sticker[0][1] + dp[1][0];
            dp[1][1] = sticker[1][1] + dp[0][0];
        }

        for(int i=2; i<sticker_num; i++) {
            dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2]);
            dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2]);
        }

        int result;
        if(sticker_num > 0) {
            result = max(dp[0][sticker_num-1], dp[1][sticker_num-1]);
        }
        
        cout << result << endl;

        caseCount--;
    }

    return 0;
}