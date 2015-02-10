#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

int main()
{
	int c;
	int cnt_ws = 0;
	int cnt_lc = 0;
	int cnt_uc = 0;
	int cnt_sym = 0;
	while ((c = getchar()) != EOF) {
		if (c == '\n') {
			break;
		} else if (c == '_') {
			++cnt_ws;
		} else if (islower(c)){
			++cnt_lc;
		} else if (isupper(c)){
			++cnt_uc;
		} else {
			++cnt_sym;
		}
	}
	int sum = cnt_ws + cnt_lc + cnt_uc + cnt_sym;
	double rat_ws = cnt_ws / (double) sum;
	double rat_lc = cnt_lc / (double) sum;
	double rat_uc = cnt_uc / (double) sum;
	double rat_sym = cnt_sym / (double) sum;
	printf("%.16f\n%.16f\n%.16f\n%.16f\n", rat_ws, rat_lc, rat_uc, rat_sym);
	return EXIT_SUCCESS;
}
