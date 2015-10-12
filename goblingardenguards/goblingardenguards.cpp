#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

class Goblin {
	public:
		int x;
		int y;
		int count;

		Goblin(int x, int y, int count = 1) {
			this->x = x;
			this->y = y;
			this->count = count;
		}

		bool operator<(const Goblin& rhs) const {
			return this->x * 10001 + this->y < rhs.x * 10001 + rhs.y;
		}

		bool operator>(const Goblin& rhs) const {
			return rhs < *this;
		}
};

ostream& operator<<(ostream& os, const Goblin& g) {
	return os << "(" << g.x << ", " << g.y << "): " << g.count;
}

bool in_range(const Goblin& g, int x, int y, int r) {
	return sqrt((g.x - x)*(g.x - x) + (g.y - y)*(g.y - y)) <= r;
}

int main() {
	int nbr_goblins;
	cin >> nbr_goblins;
	set<Goblin> goblins;

	for (int i = 0; i < nbr_goblins; i++) {
		int x, y;
		cin >> x >> y;
		Goblin g(x,y);
		pair<set<Goblin>::iterator, bool> res = goblins.insert(g);
		if (!res.second) {
			g.count += res.first->count;
			goblins.erase(res.first);
			goblins.insert(++res.first, g);
		}
	}

	int count = 0;
	int nbr_sprinklers;
	cin >> nbr_sprinklers;
	for (int i = 0; i < nbr_sprinklers; i++) {
		int x, y, r, xmin, xmax, ymin, ymax;
		cin >> x >> y >> r;
		xmin = max(x - r, 0);
		xmax = min(x + r, 10000);
		ymin = max(y - r, 0);
		ymax = min(y + r, 10000);

		for (int xi = xmin; xi <= xmax; ++xi) {
			Goblin finder(xi, ymin, 0);
			pair<set<Goblin>::iterator, bool> res = goblins.insert(finder);
			set<Goblin>::iterator it = res.first;
			set<Goblin>::iterator first;
			bool found = false;
			if (res.second) {
				goblins.erase(it++);
			}

			for (; it != goblins.end() && it->x == xi && it->y <= ymax; ++it) {
				if (in_range(*it, x, y, r)) {
					if (!found) {
						first = it;
					}
					found = true;
					count += it->count;
				} else if (found) {
					break;
				}
			}
			if (found) {
				goblins.erase(first, it);
			}

		}

	}

	cout << nbr_goblins - count << endl;
	return 0;
}
