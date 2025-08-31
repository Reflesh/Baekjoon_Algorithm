#include <stdio.h>
#include <string.h>

#define MAX_SIZE 50

int field[MAX_SIZE][MAX_SIZE];
int width, length;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

void dfs(int x, int y) {
    if (x < 0 || x >= width || y < 0 || y >= length) {
        return;
    }

    if (field[y][x] == 1) {
        field[y][x] = 0;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            dfs(nx, ny);
        }
    }
}

int main() {
    int num;
    scanf("%d", &num);

    while (num--) {
        int cab_num;
        scanf("%d %d %d", &width, &length, &cab_num);

        memset(field, 0, sizeof(field)); // 0으로 초기화

        for (int i = 0; i < cab_num; i++) {
            int index_x, index_y;
            scanf("%d %d", &index_x, &index_y);
            field[index_y][index_x] = 1;
        }

        int count = 0;
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < width; j++) {
                if (field[i][j] == 1) {
                    dfs(j, i);
                    count++;
                }
            }
        }
        printf("%d\n", count);
    }

    return 0;
}