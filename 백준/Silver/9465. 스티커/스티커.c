#include <stdio.h>

#define MAX 100000

int main() {
    int caseCount;
    scanf("%d", &caseCount);

    while(caseCount) {
        int sticker_num;
        int sticker[2][MAX];
        int dp[2][MAX];
        scanf("%d", &sticker_num);

        for(int i=0; i<2; i++) {
            for(int j=0; j<sticker_num; j++) {
                scanf("%d", &sticker[i][j]);
            }
        }

        dp[0][0] = sticker[0][0];
        dp[1][0] = sticker[1][0];

        if(sticker_num > 1) {
            dp[0][1] = sticker[0][1] + dp[1][0];
            dp[1][1] = sticker[1][1] + dp[0][0];
        }

        for (int i=2; i<sticker_num; i++) {
            dp[0][i] = sticker[0][i] + (dp[1][i-1] > dp[1][i-2] ? dp[1][i-1] : dp[1][i-2]);
            dp[1][i] = sticker[1][i] + (dp[0][i-1] > dp[0][i-2] ? dp[0][i-1] : dp[0][i-2]);
        }

        int result = (dp[0][sticker_num-1] > dp[1][sticker_num-1]) ? dp[0][sticker_num-1] : dp[1][sticker_num-1];
        printf("%d\n", result);

        caseCount--;
    }
    return 0;
}