#include <stdio.h>

int main(){
    long long int num = 1;
    int n;
    
    scanf("%d", &n);
    for(int i = 1 ; i <= n ; i++){
        num *= i;
    }
    num = num / 604800;
    printf("%lld", num);
}