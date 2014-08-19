#include <stdlib.h>
#include <stdio.h>
#include <math.h>

typedef struct bitset {
	size_t n_parts;
	unsigned int *parts; // 0 == prime, 1== nonprime
} bitset;

typedef struct res_t {
	size_t n_primes;
	bitset *bits;
} res_t;

static inline size_t part_index(size_t pos)
{
	return pos / (sizeof(unsigned int) * 8);
}

static inline size_t bit_index(size_t pos)
{
	return pos % (sizeof(unsigned int) * 8);
}

static inline void bitset_set(bitset *bits, size_t pos)
{
	bits->parts[part_index(pos)] |= 0x1 << bit_index(pos);
}

static inline unsigned char bitset_get(bitset *bits, size_t pos)
{
	return (bits->parts[part_index(pos)] >> bit_index(pos)) & 0x1;
}

res_t *getsieve(int n)
{
	res_t * r = malloc(sizeof(res_t));
	r->n_primes = n - 2;
	r->bits = malloc(sizeof(bitset));
	r->bits->n_parts =
		(int) ceil(((double) (n + 1)) / (sizeof(unsigned int) * 8));
	r->bits->parts = calloc(r->bits->n_parts, sizeof (unsigned int));

	bitset_set(r->bits, 0);
	bitset_set(r->bits, 1);

	for (int i = 2; i < (int) ceil(sqrt(n)); ++i) {
		if (bitset_get(r->bits, i) == 1) {
			continue;
		}
		for (int j = i*i; j < n; j += i) {
			if (bitset_get(r->bits, j) == 0) {
				r->n_primes--;
				bitset_set(r->bits, j);
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
	res_t *r = getsieve(n);
	printf("%zu\n", r->n_primes);

	int p;
	for (int i =0; i < q; ++i) {
		scanf("%d\n", &p);
		if (bitset_get(r->bits, p) == 0) {
			printf("1\n");
		} else {
			printf("0\n");
		}

	}
	free(r->bits->parts);
	free(r->bits);
	free(r);
	r = NULL;
        return EXIT_SUCCESS;
}
