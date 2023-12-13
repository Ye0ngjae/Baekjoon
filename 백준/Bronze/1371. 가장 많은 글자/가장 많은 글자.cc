#include <stdio.h>
#include <string.h>

int main() {
    char value[99999];
    int count[26] = {0};
    int max = 0;

    while (scanf("%[^\n]s", value) != EOF) {
        getchar();  // Consume the newline character
        for (int i = 0; i < strlen(value); i++) {
            if (value[i] >= 'a' && value[i] <= 'z') {
                count[value[i] - 'a']++;
            }
        }
    }

    for (int i = 0; i < 26; i++) {
        if (max < count[i]) {
            max = count[i];
        }
    }

    for (int i = 0; i < 26; i++) {
        if (count[i] == max) {
            printf("%c", i + 'a');
        }
    }

    return 0;
}