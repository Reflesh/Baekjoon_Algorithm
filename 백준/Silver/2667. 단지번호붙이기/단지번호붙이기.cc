#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int mapsize;
vector<vector<int>> complexMap;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int count_per_complex;

void dfs(int x, int y) {
    if (x < 0 || x >= mapsize || y < 0 || y >= mapsize) {
        return;
    }
    
    if (complexMap[x][y] == 0) {
        return;
    }
    
    complexMap[x][y] = 0;
    count_per_complex++;
    
    for (int i = 0; i < 4; i++) {
        int next_x = x + dx[i];
        int next_y = y + dy[i];
        dfs(next_x, next_y);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> mapsize;
    
    complexMap.resize(mapsize, vector<int>(mapsize));
    for (int i = 0; i < mapsize; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < mapsize; j++) {
            complexMap[i][j] = row[j] - '0';
        }
    }
    
    vector<int> result;
    
    for (int i = 0; i < mapsize; i++) {
        for (int j = 0; j < mapsize; j++) {
            if (complexMap[i][j] == 1) {
                count_per_complex = 0;
                dfs(i, j);
                result.push_back(count_per_complex);
            }
        }
    }
    
    sort(result.begin(), result.end());
    
    cout << result.size() << "\n";
    for (int count : result) {
        cout << count << "\n";
    }
    
    return 0;
}