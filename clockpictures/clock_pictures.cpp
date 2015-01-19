#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

/** @brief Compute the Knuth-Morris-Pratt substring search table.

    @param word The word to construct the table for.
    @return The kmp table.
*/
vector<int> kmp_table(vector<unsigned> word)
{
    vector<int> t(word.size());
    t[0] = -1;
    t[1] = 0;
    size_t pos = 2;
    size_t cnd = 0;
    while (pos < word.size()) {
        if (word[pos - 1] == word[cnd]) {
            // Case 1: The substring continues.
            cnd++;
            t[pos++] = cnd;
        } else if (cnd > 0) {
            // Case 2: The substring does not continue but we can fall back.
            cnd = t[cnd];
        } else {
            // Case 3: We have run out of candidates.
            t[pos++] = 0;
        }
    }
    return t;
}

/** @brief Execute the Knuth-orris-Pratt substring search.

    @param text The text where we will look for the substring.
    @param word The substring we are looking for.
    @return True if the substring was found, false otherwise.
*/
bool kmp_search(vector<unsigned> text, vector<unsigned> word)
{
    size_t m = 0;
    size_t i = 0;
    vector<int> t = kmp_table(word);
    while (m + i < text.size()) {
        if (word[i] == text[m + i]) {
            if (i == word.size() - 1)
                return true; // m is the beginning of the match.
            i++;
        } else {
            if (t[i] > -1) {
                m += i - t[i];
                i = t[i];
            } else {
                i = 0;
                m++;
            }
        }
    }
    return false;
}

int main(void)
{
    size_t n = 0;
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
    unsigned tmp0 = cl0[0];
    unsigned tmp1 = cl1[0];
    for (size_t i = 0; i < n - 1; ++i) {
        cl0[i] = cl0[i + 1] - cl0[i];
        cl1[i] = cl1[i + 1] - cl1[i];
    }
    cl0[n - 1] = 360000 - cl0[n - 1] + tmp0;
    cl1[n - 1] = 360000 - cl1[n - 1] + tmp1;

    // Duplicate the first clock face.
    vector<unsigned> cl2(cl0.begin(), cl0.end());
    cl2.insert(cl2.end(), cl0.begin(), cl0.end());

    // Execute the substring-search.
    if (kmp_search(cl2, cl1))
        cout << "possible" << endl;
    else
        cout << "impossible" << endl;

    return 0;
}
