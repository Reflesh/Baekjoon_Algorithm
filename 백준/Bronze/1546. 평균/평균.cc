#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int num;
    cin >> num;
    
    vector<float> grade(num, 0);
    for(int i = 0; i < num; i++) {
        cin >> grade[i];
    }
    int max_grade;
    max_grade = *max_element(grade.begin(), grade.end());
    // cout << max_grade << endl;
    for(int i = 0; i < num; i++) {
        grade[i] = grade[i] / max_grade * 100;
    }
    float grade_sum;
    for(int i = 0; i < num; i++) {
        grade_sum += grade[i];
    }
    cout << grade_sum / num << endl;

    return 0;

}