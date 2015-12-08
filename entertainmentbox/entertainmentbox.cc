#include <iostream>
#include <set>
#include <numeric>

using namespace std;

class Show {
	public:
		int start;
		int stop;
		int id;

		Show(int start, int stop, int id) {
			this->start = start;
			this->stop = stop;
			this->id = id;
		}

		bool operator<(const Show& rhs) const {
			return this->stop == rhs.stop ? this->id < rhs.id : this->stop < rhs.stop;
		}

		bool operator>(const Show& rhs) const {
			return rhs < *this;
		}
};

ostream& operator<<(ostream& os, const Show& g) {
	return os << "[" << g.start << ", " << g.stop << "]: " << g.id;
}

class Recorder {
	public:
		int end;

		Recorder() : end(0) { }
};

int main(int argc, const char *argv[])
{
	int n, k;
	cin >> n >> k;
	set<Show> shows;
	Recorder *recorders = new Recorder[k];

	while (n) {
		int start, stop;
		cin >> start >> stop;
		Show show(start, stop, n);
		shows.insert(show);
		n--;
	}

	int count = 0;

	for (set<Show>::iterator iter = shows.begin(); iter != shows.end(); ++iter) {
		const Show &show = *iter;
		auto tmp = [show](Recorder *best, Recorder &rec) -> Recorder* {
			if ((best->end > show.start && rec.end <= show.start) || (rec.end > best->end && rec.end <= show.start)) {
				return &rec;
			} else {
				return best;
			}
		};

		Recorder *best = accumulate(recorders, recorders + k, recorders, tmp);
		if (best->end <= show.start) {
			best->end = show.stop;
			++count;
		}
	}

	cout << count << endl;

	return 0;
}
