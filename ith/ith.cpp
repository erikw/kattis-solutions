#include <vector>
#include <iostream>
#include <utility>
#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

struct ChessBoard {

    ChessBoard(int sx, int sy) : sx(sx),
                                 sy(sy),
                                 queens(),
                                 rows(sy, true),
                                 cols(sx, true),
                                 pdiag_pos(sy, true),
                                 pdiag_neg(sx, true),
                                 sdiag_pos(sy, true),
                                 sdiag_neg(sx, true) {}
    ~ChessBoard() {}

    void AddQueen(int x, int y) {
        //queens.insert(make_pair(x, y));
        rows[y] = false;
        cols[x] = false;
        if (x - y >= 0)
            pdiag_pos[x - y] = false;
        else
            pdiag_neg[y - x] = false;
        if (sx - 1 - x - y >= 0)
            sdiag_pos[sx - 1 - x - y] = false;
        else
            sdiag_neg[abs(sx - 1 - x - y)] = false;
    }

    bool IsFreeSquare(int x, int y) {
        if (!rows[y])
            return false;
        if (!cols[x])
            return false;
        if (x - y >= 0 && !pdiag_pos[x - y])
            return false;
        if (x - y < 0 && !pdiag_neg[y - x])
            return false;
        if (sx - 1 - x - y >= 0 && !sdiag_pos[sx - 1 - x - y])
            return false;
        if (sx - 1 - x - y < 0 && !sdiag_neg[abs(sx - 1 - y - x)])
            return false;
        return true;
    }

    int CountFreeSquares() {
        int cnt = 0;
        for (int y = 0; y < sy; ++y) {
            for (int x = 0; x < sx; ++x) {
                cnt += IsFreeSquare(x, y);
            }
        }
        return cnt;
    }

    void PrintBoard() {
        for (int y = 0; y < sy; ++y) {
            for (int x = 0; x < sx; ++x) {
                set<pair<int,int> >::iterator it = queens.find(make_pair(x, y));
                if (it != queens.end())
                    cout << "Q" << " ";
                else
                    cout << !IsFreeSquare(x, y) << " ";
            }
            cout << endl;
        }
    }

    int sx;
    int sy;
    set<pair<int, int> > queens;

    vector<bool> rows;
    vector<bool> cols;

    vector<bool> pdiag_pos;
    vector<bool> pdiag_neg;

    vector<bool> sdiag_pos;
    vector<bool> sdiag_neg;
};


int main(void) {

    while (true) {
        int x = 0, y = 0, n = 0;
        (void)scanf("%d %d %d\n", &x, &y, &n);

        ChessBoard board(x, y);
        //printf("%d %d %d\n", x, y, n);
        if (x == 0 && y == 0 && n == 0)
            return 0;

        // Add the queens
        for (int i = 0; i < n; ++i) {
            int qx = 0, qy = 0;
            (void)scanf("%d %d", &qx, &qy);
            board.AddQueen(qx - 1, qy - 1);
            //printf("%d %d\n", qx, qy);
        }

        int cnt = board.CountFreeSquares();
        //board.PrintBoard();
        cout << cnt << endl;

    }

    return 0;
}
