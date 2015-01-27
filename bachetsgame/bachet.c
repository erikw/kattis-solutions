#include <stdlib.h>
#include <stdio.h>


int can_win(int i, size_t m, int *nbrs, int *wins)
{
	for (size_t n_idx = 0; n_idx < m; ++n_idx) {
		if (nbrs[n_idx] <= i) {
			if (!wins[i - nbrs[n_idx]]) {
				return 1;
			}
		}
	}
	return 0;
}

int main()
{

	while (1) {
		size_t n;
		size_t m;
		int *nbrs;
		int nscan = scanf("%zu", &n);
		if (nscan == EOF) {
			break;
		} else if (nscan != 1) {
			return EXIT_FAILURE;
		}
		nscan = scanf("%zu", &m);
		if (nscan != 1) {
			return EXIT_FAILURE;
		}
		nbrs = malloc(m * sizeof(int));
		if (nbrs == NULL) {
			return EXIT_FAILURE;
		}
		for (size_t i = 0; i < m; i++) {
			nscan = scanf("%d", &nbrs[i]);
			if (nscan != 1) {
				return EXIT_FAILURE;
			}
		}


		int *wins = calloc(n + 1, sizeof(int));
		for (size_t i = 1; i <= n; i++) {
			wins[i] = can_win(i, m, nbrs, wins);
		}
		if (wins[n]) {
			printf("Stan wins\n");
		} else {
			printf("Ollie wins\n");
		}
		free(wins);
		free(nbrs);
	}

	return EXIT_SUCCESS;
}
