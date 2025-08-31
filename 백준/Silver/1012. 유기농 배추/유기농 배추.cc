#include <iostream>
#include <vector>
using namespace std;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

void dfs(int x, int y, vector<vector<int>>& field) {
    int width = field[0].size();
    int length = field.size();

    if(x < 0 || x >= width || y < 0 || y >= length) {
        return;
    }

    if(field[y][x] == 1) {
        field[y][x] = 0;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            dfs(nx, ny, field);
        }
    }
    
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num;
    cin >> num;

    while(num--) {
        int width, length, cab_num;
        cin >> width >> length >> cab_num;

        vector<vector<int>> field(length, vector<int>(width, 0));

        for(int i = 0; i < cab_num; i++) {
            int index_x, index_y;
            cin >> index_x >> index_y;
            field[index_y][index_x] = 1;
        }

        int count = 0;
        for(int i = 0; i < length; i++) {
            for(int j = 0; j < width; j++) {
                if(field[i][j] == 1) {
                    dfs(j, i, field);
                    count++;
                }
            }
        }
        cout << count << endl;
    }

    return 0;
}