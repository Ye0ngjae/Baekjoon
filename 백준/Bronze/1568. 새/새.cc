#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int i;
	int n, count;

	scanf("%d", &n);

	count = 0;

	while (n > 0)
	{
		for (i = 1; i <= n; i++)
		{
			count++;
			n -= i;
		}
	}

	printf("%d", count);

	return 0;
}