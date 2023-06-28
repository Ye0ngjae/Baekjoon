#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int n;
	double fir = 0, sec = 0 ;
	vector<pair<double,double>> pos;
	scanf("%d", &n);
	for ( int i = 0 ; i < n ; i++){
		double x, y;
		scanf("%lf %lf", &x, &y);
		pos.push_back({ x, y });
	}
	pos.push_back(pos[0]);
	for ( int i = 0; i < n ; i++)
		fir += (pos[i].first * pos[i + 1].second);
	for(int i = 1 ; i <= n; i++)
		sec += (pos[i].first * pos[i - 1].second);
	printf("%.1lf\n", (double)abs(fir - sec) * 0.5);
}