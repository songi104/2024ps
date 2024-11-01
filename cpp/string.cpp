#include <iostream>

using namespace std;


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string str = "hello worlld";
    str += " I am..";
    cout << str << '\n';

    cout << str.find("ll", 2); // find(찾는 것, 어디부터);

    return 0;
}