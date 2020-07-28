#include <bits/stdc++.h>

using namespace std;

int main() {


	int n;
	cin >> n;
	vector<int> x(n);
	for (int i = 0; i < n; ++i) {
		cin >> x[i];
	}

	sort(x.begin(), x.end());
	vector<int> a = { x[0] };

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < 31; ++j) {
			int left = x[i] - pow(2,j);
			int right = x[i] + pow(2,j);
			bool left1 = binary_search(x.begin(), x.end(), left);
			bool right1 = binary_search(x.begin(), x.end(), right);
			if (left1 && right1 && int(a.size()) < 3) {
				a = { left, x[i], right };
			}
			if (left1 && int(a.size()) < 2) {
				a = { left, x[i] };
			}
			if (right1 && int(a.size()) < 2) {
				a = { x[i], right };
			}
		}
	}

	cout << int(a.size()) << endl;
	for (auto i : a)
		cout << i<< " ";
	cout << endl;

	return 0;
}
