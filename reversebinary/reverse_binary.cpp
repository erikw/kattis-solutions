#include <iostream>
#include <cstdint>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

/** @brief Count the number of leading zeroes.

    @param i The number to count the number of leading zeroes in.
    @return The number of leading zeroes.
*/
uint8_t clz32(uint32_t i)
{
    uint32_t x;
    size_t n;
    size_t c;

    n = 32;
    c = 32 >> 1;
    do {
        x = i >> c;
        if (x != 0) {
            n = n - c;
            i = x;
        }
        c >>= 1;
    } while (c != 0);

    return n - i;
}

/** @brief Compute log-2 of a 32 bit binary number.

    @param i The number to compute the logarithm of.
    @return The number of leading zeroes.
*/
uint8_t log2(uint32_t i)
{
    return 32 - clz32(i);
}

/** @brief Reverse a 32-bit unsigned integer.

    @param x The binary number to be reversed.
    @param n Maximum number of bits to reverse.
    @return The number with all bits reversed.
*/
uint32_t rev32(uint32_t x, int8_t n = 32)
{
    static uint8_t table[16] = {0x0, 0x8, 0x4, 0xC,
                                0x2, 0xA, 0x6, 0xE,
                                0x1, 0x9, 0x5, 0xD,
                                0x3, 0xB, 0x7, 0xF};
    uint32_t r = 0;
    uint8_t revs = (n + 4 - 1) / 4;
    for (int8_t i = revs - 1; i >= 0; i--) {
        r = (r << 4) + table[x & 0xF];
        x >>= 4;
    }
    return r >> (revs * 4 - n);
}

int main(void)
{
    uint32_t n = 0;
    cin >> n;
    cout << rev32(n, log2(n)) << endl;
    return 0;
}
