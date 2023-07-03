#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

  char arr[100];
  char arr1[50], arr2[50];

  scanf("%s", arr);

  int index = strlen(arr), q;
  int sw = 1;

  for(int i = 0 ; i < index / 2; i++){
    if(arr[i] != arr[index - 1 -i]){
      sw = 0;
    }
  }
      
  if(sw == 1){
    printf("1");  
  }
  else{
    printf("0");
  }
    
	return 0;
}