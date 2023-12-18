#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main(){
    while(1){
        char str[8];
        int num[8], result = 0;
        scanf("%s", str);
        getchar();
        if(str[0] == '#'){
            break;
        }
        
        int len = strlen(str);
        
        for(int i = 0 ; i < len ; i++){
            switch(str[i]){
                case '-':
                    num[i] = 0;
                    break;
                case '\\':
                    num[i] = 1;
                    break;
                case '(':
                    num[i] = 2;
                    break;
                case '@':
                    num[i] = 3;
                    break;
                case '?':
                    num[i] = 4;
                    break;
                case '>':
                    num[i] = 5;
                    break;
                case '&':
                    num[i] = 6;
                    break;
                case '%':
                    num[i] = 7;
                    break;
                case '/':
                    num[i] = -1;
                    break;
            }
        }
        for(int i = 0 ; i < len ; i++){
            result += num[i] * pow(8,len-i-1);
        }
        printf("%d\n", result);
    }

    return 0;
}
