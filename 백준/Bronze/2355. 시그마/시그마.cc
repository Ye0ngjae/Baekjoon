#include <stdio.h>
#include <math.h>

int main()
{
    long long int a,b;
    long long int sum;
    
    scanf("%lld %lld", &a, &b);
    
    if(a < b){
        sum = (b - a + 1) * (a + b) / 2;
    }
    else{
        sum = (a - b + 1) * (a + b) / 2;
    }
    
    printf("%lld", sum);

    return 0;
}
