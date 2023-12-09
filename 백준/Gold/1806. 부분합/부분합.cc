#include <stdio.h>
#pragma warning(disable: 4996)
#ifndef min
#define min(a,b)  (((a) < (b)) ? (a) : (b))
#endif
#define _CRT_SECURE_NO_WARNINGS

int main() {

    int N, S;
    int arr[100000];

    scanf("%d %d", &N, &S);
    for (int i = 0; i < N; i++) 
        scanf("%d", &arr[i]);

    int s = 0, e = 0, sum = 0, ans = 987654321;

    while (1) {
        if (sum >= S) {
            ans = min(ans, e - s);
            sum -= arr[s++];
        }
        else if (e == N) 
            break;
        else 
            sum += arr[e++];
    }
    printf("%d", ans == 987654321 ? 0 : ans);

	return 0;
}