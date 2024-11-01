#include <iostream>

using namespace std;


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string target, find; //target:대상이되는문자열 find:찾을녀석
    
    getline(cin, target);
    getline(cin, find);


    int l = target.size();
    int t = find.size();
    int i =0 ;
    int res = 0;

    while (i<l) {
        //cout <<i << ": " << target.substr(i, i+t) <<'\n';
        
        if (find == target.substr(i, t)) {
            i += t;
            res ++;
        } else i++;
    }
    cout << res;

    return 0;
}