#include <iostream>

using namespace std;



int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    string pattern;
    cin >> n;
    cin >> pattern;

    string front, back; //앞에 몇개 뒤에 몇개 ab*cd는 2,2
    front = pattern.substr(0, pattern.find("*"));
    back = pattern.substr(front.size()+1, pattern.size() - front.size());
    //cout << front <<'\n' << back;

    while (n--) {
        string line;
        cin >> line;

        // 앞에 확인
        bool b1;
        if (line.find(front) == 0) {
            b1=true;
        } else b1=false;

        // 뒤에 확인
        bool b2 = false;
        int pos = line.find(back);
        while (pos != string::npos) {
            if (pos == line.size()-back.size()) {
                b2= true;
                break;
            }
            pos = line.find(back, pos+back.size());
        }
        
        if (pos == front.size()) b2=false;

        if (b1&&b2) cout << "DA\n";
        else cout << "NE\n";


    }

    return 0;
}