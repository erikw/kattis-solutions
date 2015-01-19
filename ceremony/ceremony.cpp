#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

int main(void)
{
	std::vector<int> houses;
	int n;
	int d = 0;
	int res = 0;
	int min = 0;

	if (scanf("%d\n", &n) != 1) {
		fprintf(stderr, "Baah.");
		return EXIT_FAILURE;
	}
	int max = n - 1;

	for (int i = 0; i < n; ++i) {
		int tmp;
		if (scanf("%d", &tmp) != 1) {
			fprintf(stderr, "Baah.");
			return EXIT_FAILURE;
		}
		houses.push_back(tmp);
	}

	sort(houses.begin(), houses.end());

	while (min <= max) {
		int maxh = houses[max] - d;
		int l = max - min + 1;

		if (l > maxh) {
			++d;
			while (houses[min] - d <= 0 && min <= max)
				++min;
		} else {
			--max;
		}
		++res;
	}

	printf("%d\n", res);

	return EXIT_SUCCESS;
}
