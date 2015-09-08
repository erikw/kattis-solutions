#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int popcnt(char ch)
{
	int sum = 0;
	for (size_t i = 0; i < 7; i++)
	{
		sum += (ch >> i) & 1;
	}
	return sum;
}

int main()
{
	while (true)
	{
		char buf[101];
		size_t i = 0;
		size_t sum = 0;

		if (fgets(buf, 101, stdin) == NULL)
		{
			break;
		}

		while (buf[i] != '\n' && buf[i] != '\0')
		{
			sum += popcnt(buf[i++]);
		}
		if (sum % 2 || 7 * (strlen(buf) - 1) % 2)
		{
			printf("trapped\n");
		}
		else
		{
			printf("free\n");
		}
	}
	return 0;
}
