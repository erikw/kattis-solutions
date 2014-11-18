#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

/** @brief Test if the first range is circularly equal with the second one.

    @param first1 The first element of the first sequence.
    @param start1 The starting element for the first sequence.
    @param last1 The last element of the first sequence.
    @param start2 The first element of the second sequence.
    @param last2 The last element of the second sequence.
*/
template <class InputIterator1, class InputIterator2>
bool circularly_equal(
    InputIterator1 first1, InputIterator1 start1, InputIterator1 last1,
    InputIterator2 start2, InputIterator2 last2
    )
{
    while (start2 != last2) {

        if (!(*start1 == *start2))
            return false;

        ++start1;
        ++start2;

        // If we reached one past the last element, wrap around.
        if (start1 == last1)
            start1 = first1;
    }
    return true;
}


template <class InputIterator>
unsigned hash(InputIterator start, InputIterator end, unsigned p, unsigned mod)
{
    unsigned h = 0;
    unsigned power = 1;
    while (start != end) {
	h += (*start * power) % mod;
	power *= p;
	++start;
    }
    return h;
}



// Execute a circular rabin_karp_sublist_search.
bool rabin_karp_sublist_search(vector<unsigned> str, unsigned hs,
                               vector<unsigned> pat, unsigned hp,
			       unsigned power, unsigned mod)
{
    // Run Rabin Karp substring searching using a rolling hash.
    size_t n = str.size();
    size_t m = pat.size();
    for (size_t i = 0; i < n - m; ++i) {
	//cout << "hs=" << hs << " hp=" << hp << " power=" << power << endl;
        if (hs == hp) {
            if (equal(str.begin(), str.begin() + i, pat.begin()))
                return true; // Could also return index here.
        }
        //hs = hs - str[i] + str[(i + m) % n];
        hs = (11 * (hs - str[i]*power % mod) + str[(i + m)]) % mod;
	//cout << "hs=" << hs << " hash=" << hash(str.rbegin() + i, str.rbegin() + i + m, 11, mod) << endl;
    }
    return false;
}


int main(void)
{
    size_t n = 0;
    unsigned p = 27644437; // A large prime.
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

    // Compute angle differences and intial sum hashes.
    unsigned hs = 0;
    unsigned hp = 0;
    unsigned tmp0 = cl0[0];
    unsigned tmp1 = cl0[0];
    for (size_t i = 0; i < n - 1; ++i) {
        cl0[i] = cl0[i + 1] - cl0[i];
        cl1[i] = cl1[i + 1] - cl1[i];
    }
    cl0[n - 1] = 360000 - cl0[n - 1] + tmp0;
    cl1[n - 1] = 360000 - cl1[n - 1] + tmp1;

    // Compute the hashes.
    unsigned power = 1;
    for (ssize_t i = n - 1; i > 0; --i) {
	hs += cl0[i] * power % p;
	hp += cl1[i] * power % p;
	power *= 11;
    }

    vector<unsigned> cl2(2*n);
    cl2.insert(cl2.end(), cl0.begin(), cl0.end());
    cl2.insert(cl2.end(), cl0.begin(), cl0.end());

    // cout << "hp=" << hp << " hash=" << hash(cl1.rbegin(), cl1.rend(), 11, p) << endl;
    // cout << "hs=" << hs << " hash=" << hash(cl2.rbegin(), cl2.rbegin() + n, 11, p) << endl << endl;


    if (rabin_karp_sublist_search(cl2, hs, cl1, hp, power, p))
        cout << "possible" << endl;
    else
        cout << "impossible" << endl;

    return 0;
}
