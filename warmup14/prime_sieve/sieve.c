#include <stdlib.h>
#include <stdio.h>
#include <math.h>

struct res {
	unsigned char *sieve; // 0 == prime, 1== nonprime
	size_t n_primes;
};

struct res *
getsieve(int n) {
	struct res * r = malloc(sizeof(struct res));
	r->n_primes = n - 2;
	r->sieve = malloc(n);
	r->sieve[0] = 1;
	r->sieve[1] = 1;

	for (int i = 2; i < (int) ceil(sqrt(n)); ++i) {
		if (r->sieve[i] == 1) {
			continue;
		}
		for (int j = i*i; j < n; j += i) {
			if (r->sieve[j] != 1) {
				r->n_primes--;
				r->sieve[j] = 1;
			}
		}
	}
	return r;
}

int main(void)
{
	int n, q;        
	scanf("%d %d\n", &n, &q);
	++n;
	struct res *r = getsieve(n);
	printf("%zu\n", r->n_primes);
	
	int p;
	for (int i =0; i < q; ++i) {
		scanf("%d\n", &p);
		if (r->sieve[p] == 0) {
			printf("1\n");
		} else {
			printf("0\n");
		}

	}
	free(r->sieve);
	free(r);
	r = NULL;
        return EXIT_SUCCESS;
}
