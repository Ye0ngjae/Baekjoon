#include<bits/stdc++.h>
using namespace std;
using ll = long long;

ll n, s, x;

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);
    cin >> n;
    while(n--){
        int a, b; cin >> a;
        if(a == 1){
            cin >> b;
            s += b, x ^= b;
        }
        if(a == 2){
            cin >> b;
            s -= b, x ^= b;
        }
        if(a == 3){
            cout << s << '\n';
        }
        if(a == 4){
            cout << x << '\n';
        }
    }
}