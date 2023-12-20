#include <stdio.h>

int main() {
    int arr[8];

    for (int i = 0; i < 8; i++) {
        scanf("%d", &arr[i]);
    }

    int asc = 1, desc = 1; // 초기값을 1로 설정

    for (int i = 0; i < 7; i++) {
        if (arr[i] < arr[i + 1]) {
            desc = 0; // 현재 원소보다 다음 원소가 크면 desc는 0
        } else if (arr[i] > arr[i + 1]) {
            asc = 0; // 현재 원소보다 다음 원소가 작으면 asc는 0
        }
    }

    if (asc) {
        printf("ascending");
    } else if (desc) {
        printf("descending");
    } else {
        printf("mixed");
    }

    return 0;
}