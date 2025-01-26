#include <iostream>
using namespace std;

int main() {
    string major, grade;
    float credit;
    double avg = 0;
    float sum_credit = 0;

    for(int i = 0; i < 20; i++) {
        float score;
        cin >> major >> credit >> grade;
        if(grade == "A+")
            score = credit * 4.5;
        else if(grade == "A0")
            score = credit * 4.0;
        else if(grade == "B+")
            score = credit * 3.5;
        else if(grade == "B0")
            score = credit * 3.0;
        else if(grade == "C+")
            score = credit * 2.5;
        else if(grade == "C0")
            score = credit * 2.0;
        else if(grade == "D+")
            score = credit * 1.5;
        else if(grade == "D0")
            score = credit * 1.0;
        else if(grade == "P") {
            score = credit * 0.0;
            credit = 0.0; // 학점이 P인 경우 계산에서 제외
        }
        else if(grade == "F")
            score = credit * 0.0;
        avg += score;
        sum_credit += credit;
        //cout << "i : " << i  << " -> avg : " << avg << ", sum_credit : " << sum_credit << endl;
    }

    avg /= sum_credit;
    cout << avg << endl;

    return 0;
}