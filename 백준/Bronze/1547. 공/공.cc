#include <stdio.h>

int main(){
    int ball[3] = { 1,0,0 };
    int num, a, b, a1, b1, temp;
    //printf("[%d %d %d]\n", ball[0], ball[1], ball[2]);
    scanf("%d", &num);
    
    for(int i = 0 ; i < num ; i++){
        scanf("%d %d", &a, &b);
        temp = ball[a-1];
        a1 = ball[b-1];
        b1 = temp;
        ball[a-1] = a1;
        ball[b-1] = b1;
        //printf("a : %d b: %d, temp: %d\n", a,b,temp);
        //printf("[%d %d %d]\n", ball[0], ball[1], ball[2]);
    }
    for(int i = 0 ; i < 3 ; i++){
        if(ball[i] == 1){
            printf("%d", i+1);
        }
    }
    return 0;
}