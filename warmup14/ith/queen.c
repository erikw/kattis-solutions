
#include <stdlib.h>
#include <stdio.h>
#include <math.h>


#define forever for(;;)

#define min(x,y) ((x) > (y) ? (y) : (x))
#define max(x,y) min(y,x)

typedef struct bitmat {
	size_t x, y;
	size_t cap;		/* Number of allocated bytes. */
	size_t n_bits;		/* Number of bits used. */
	unsigned char 	*data;
} bitmat;

static inline size_t part_index(size_t pos)
{
	return pos / 8;
}

static inline size_t bit_index(size_t pos)
{
	return pos % 8;
}

static inline size_t c2i(bitmat *mat, size_t x, size_t y)
{
	return y * mat->x + x;
}

static inline void bitmat_set(bitmat *bits, size_t pos)
{
	bits->data[part_index(pos)] |= 0x1 << bit_index(pos);
}

static inline unsigned char bitmat_get(bitmat *bits, size_t pos)
{
	return (bits->data[part_index(pos)] >> bit_index(pos)) & 0x1;
}

static void bitmat_print(bitmat *mat)
{
	size_t x, y;

	for (y = 0; y < mat->y; ++y) {
		for (x = 0; x < mat->x; ++x) {
			printf("%d ", bitmat_get(mat, c2i(mat, x, y)));
		}
		printf("\n");
	}
}

static void bitmat_set_diag_rise(bitmat *mat, size_t qx, size_t qy)
{
	int y;
	size_t x;
	size_t m;

	m = qy + qx;
	y = min(m, mat->y - 1);
	x = m - y;
	for (; x < mat->x && y >= 0; ++x, --y) {
		bitmat_set(mat, c2i(mat, x, y));
	}

}

static void bitmat_set_diag_fall(bitmat *mat, size_t qx, size_t qy)
{
	size_t y;
	int m;
	int x;

	m = qy - qx;
	y = m;
	x = max(y - m, 0);
	printf("qx = %zu, qy = %zu, m=%zu\n", qx, qy, m);
	printf("y = %zu\n", y);
	printf("x = %zu\n", x);
	for (; x < mat->x && y < mat->y; ++x, ++y) {
		bitmat_set(mat, c2i(mat, x, y));
	}

}


static void bitmat_set_row(bitmat *mat, size_t row)
{
	size_t i;

	for (i = row * mat->x; i < (row + 1) * mat->x; ++i) {
		bitmat_set(mat, i);
	}
}

static void bitmat_set_col(bitmat *mat, size_t col)
{
	size_t i;

	for (i = col; i < mat->y*mat->x; i+=mat->x) {
		bitmat_set(mat, i);
	}
}

static size_t count_zeroes(bitmat *mat)
{
	size_t count = 0;

	for (size_t i = 0; i < mat->n_bits; ++i) {
		count += !bitmat_get(mat, i);
	}

	return count;
}

int main(void)
{
	bitmat mat;

	forever {
		size_t x, y, n, i;
		size_t n_bits;

		scanf("%zu %zu %zu\n", &x, &y, &n);
		if (x == 0 && y == 0 && n == 0) {
			break;
		}

		n_bits = x*y;
		mat.x = x;
		mat.y = y;
		mat.cap = (size_t) ceil(((double) n_bits / 8));
		mat.n_bits = n_bits;
		mat.data = calloc(mat.cap, 1);

		for (i = 0; i < n; ++i) {
			size_t qx, qy;

			scanf("%zu %zu\n", &qx, &qy);
			--qx;
			--qy;
			bitmat_set_row(&mat, qy);
			bitmat_set_col(&mat, qx);
			bitmat_set_diag_rise(&mat, qx, qy);
			bitmat_set_diag_fall(&mat, qx, qy);
		}

		bitmat_print(&mat);
		printf("%zu\n", count_zeroes(&mat));
		free(mat.data);
	}

	return EXIT_SUCCESS;
}
