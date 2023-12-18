#include <stdio.h>

int main(){
    int n, input;
    int num[50];
    
    scanf("%d", &n);
    
    for(int i = 0 ; i < n ; i++){
        scanf("%d", &input);
        num[i] = input;
    }
    
    if((num[2] - num[1]) == (num[1] - num[0])){
        //등차
        printf("%d", num[n-1]+(num[1] - num[0]));
    }
    else{
        //등비
        printf("%d", num[n-1] * (num[1] / num[0]));
    }

    return 0;
}
