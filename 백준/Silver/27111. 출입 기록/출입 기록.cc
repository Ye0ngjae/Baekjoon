#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cstdio>
#include <string>
#include <deque>
#include <stack>
#define P pair<int,int>
#define F first
#define S second
#define LL long long

using namespace std;

int N, number;
int check[200001];

void solve(){
    int ans = 0;
    for(int i = 1 ; i <= N; i++){
        int x, y;
        cin >> x >> y;
        number = max(number, x);
        if(y == 0){
            if(check[x] == 1) check[x] = 0;
            else ans++;
        }
        else{
            if(check[x] == 1) ans++;
            else check[x] = 1;
        }
    }
    for(int i = 1; i <= number; i++){
        if(check[i] != 0) ans++;
    }
    cout << ans;
}

int main() {
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	solve();
	return 0;
}
