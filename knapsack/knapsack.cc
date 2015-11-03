#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void knap_teh_sack(int c, int n, vector<int> &v, vector<int> &w) {
	int W = c + 1;
	int N = n + 1;
	int *m = new int[N * W];

	for (int i = 1; i < N; ++i) {
		for (int j = 0; j < W; ++j) {
			if (w[i-1] <= j) {
				m[i*W + j] = max(m[(i-1)*W + j], m[(i-1)*W + j - w[i-1]] + v[i-1]);
			} else {
				m[i*W + j] = m[(i-1)*W + j];
			}
		}
	}

	vector<int> res;
	int j = W - 1;
	for (int i = N - 1; i > 0; --i) {
		if (m[i*W + j] != m[(i-1)*W + j]) {
			res.push_back(i-1);
			j -= w[i-1];
		}
	}

	cout << res.size() << endl;
	for (auto i : res) {
		cout << i << " ";
	}
	cout << endl;
}

int main()
{
	while (!cin.eof()) {
		double c;
		int n;
		cin >> c >> n;
		if (cin.eof()) {
			break;
		}
		vector<int> v, w;

		for (int i = 0; i < n; i++) {
			int value, weight;
			cin >> value >> weight;
			v.push_back(value);
			w.push_back(weight);
		}
		knap_teh_sack(c, n, v, w);
	}
	return 0;
}
