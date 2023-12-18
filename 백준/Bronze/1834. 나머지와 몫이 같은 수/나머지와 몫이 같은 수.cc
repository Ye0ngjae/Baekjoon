#include <stdio.h>

int main(){
    long int n; 
    long int sum = 0;
    int num[50];
    
    scanf("%ld", &n);
    
    for(int i = 1 ; i < n ; i++){
        sum += (n+1)*i;
    }
    
    printf("%ld", sum);

    return 0;
}
