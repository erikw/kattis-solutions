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


// Execute a circular rabin_karp_sublist_search.
bool rabin_karp_sublist_search(vector<unsigned> str, unsigned hs,
                               vector<unsigned> pat, unsigned hp)
{
    // Run Rabin Karp substring searching using a rolling hash.
    size_t n = str.size();
    size_t m = pat.size();
    for (size_t i = 0; i < n; ++i) {
        if (hs == hp) {
            if (circularly_equal(str.begin(), str.begin() + i, str.end(),
                                 pat.begin(), pat.end()))
                return true; // Could also return index here.
        }
        hs = hs - str[i] + str[(i + m) % n];
        //hs = p_first * (hs - str[i]*p_last) + p_first * str[(i + m) % n];
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
    unsigned pow = 1;
    unsigned tmp = cl0[0];
    for (size_t i = 0; i < n - 1; ++i) {
        cl0[i] = cl0[i + 1] - cl0[i];
        hs += cl0[i];
        pow *= p;
    }
    cl0[n - 1] = 360000 - cl0[n - 1] + tmp;
    hs += cl0[n - 1];

    tmp = cl1[0];
    pow = 1;
    unsigned hp = 0;
    for (size_t i = 0; i < n - 1; ++i) {
        cl1[i] = cl1[i + 1] - cl1[i];
        hp += cl1[i];
        pow *= p;
    }
    cl1[n - 1] = 360000 - cl1[n - 1] + tmp;
    hp += cl1[n - 1];

    if (rabin_karp_sublist_search(cl0, hs, cl1, hp))
        cout << "possible" << endl;
    else
        cout << "impossible" << endl;

    return 0;
}
