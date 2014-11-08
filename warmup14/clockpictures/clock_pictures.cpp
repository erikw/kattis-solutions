#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool rabin_karp_sublist_search(vector<unsigned> str, vector<unsigned> pat)
{
    // Compute initial hashes.
    size_t n = str.size();
    size_t m = pat.size();
    unsigned hs = 0;
    unsigned hp = 0;

    for (size_t i = 0; i < m; ++i) {
        hs += str[i];
        hp += pat[i];
    }

    // Run Rabin Karp substring searching using a rolling hash.
    for (size_t i = 0; i < n - m; ++i) {
        if (hs == hp) {
            if (equal(str.begin() + i, str.begin() + m, pat.begin()))
                return true; // Could also return index here.
        }
        hs = hs - str[i] + str[i + m];
    }

    return false;
}


int main(void)
{
    size_t n = 0;
    unsigned u = 0;
    cin >> n;

    // Read all input.
    vector<unsigned> cl0(n);
    vector<unsigned> cl1(n);
    for (size_t i = 0; i < n; ++i)
        cin >> cl0[i];
    for (size_t i = 0; i < n; ++i)
        cin >> cl1[i];

    sort(cl0.begin(), cl0.end());
    sort(cl1.begin(), cl1.end());

    // Compute angle differences.
    unsigned tmp = cl0[0];
    for (size_t i = 0; i < n - 1; ++i)
        cl0[i] = cl0[i + 1] - cl0[i];
    cl0[n - 1] = 360000 - cl0[n - 1] + tmp;

    tmp = cl1[0];
    for (size_t i = 0; i < n - 1; ++i)
        cl1[i] = cl1[i + 1] - cl1[i];
    cl1[n - 1] = 360000 - cl1[n - 1] + tmp;

    // Extend the first list with itself and do a sublist search.
    vector<unsigned> seq(2*n);
    for (size_t i = 0; i < n; ++i)
        seq[i] = cl0[i];
    for (size_t i = n; i < 2*n; ++i)
        seq[i] = cl0[i - n];

    if (rabin_karp_sublist_search(seq, cl1))
        cout << "possible" << endl;
    else
        cout << "impossible" << endl;

    return 0;
}
