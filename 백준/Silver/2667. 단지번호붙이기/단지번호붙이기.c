#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 25

int size;
int complexMap[MAX_SIZE][MAX_SIZE];
int visited[MAX_SIZE][MAX_SIZE] = {0};

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int count; 

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

void dfs(int x, int y) {
    if (x < 0 || x >= size || y < 0 || y >= size) {
        return;
    }
    
    if (complexMap[x][y] == 0) {
        return;
    }
    
    complexMap[x][y] = 0;
    count++;
    
    for (int i = 0; i < 4; i++) {
        int next_x = x + dx[i];
        int next_y = y + dy[i];
        dfs(next_x, next_y);
    }
}

int main() {
    scanf("%d", &size);
    
    for (int i = 0; i < size; i++) {
        char row[MAX_SIZE];
        scanf("%s", row);
        for (int j = 0; j < size; j++) {
            complexMap[i][j] = row[j] - '0';
        }
    }
    
    int result[MAX_SIZE * MAX_SIZE];
    int complex_count = 0;
    
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (complexMap[i][j] == 1) {
                count = 0;
                dfs(i, j);
                result[complex_count++] = count;
            }
        }
    }
    
    qsort(result, complex_count, sizeof(int), compare);
    
    printf("%d\n", complex_count);
    for (int i = 0; i < complex_count; i++) {
        printf("%d\n", result[i]);
    }
    
    return 0;
}