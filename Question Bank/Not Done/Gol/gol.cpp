#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<int> a(n), b(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }

    for (int i = 0; i < q; i++) {
        int x, y;
        cin >> x >> y;
        a[x - 1] += y;
        int cost = 0;
        for (int j = 1; j < n; j++) {
            if (a[j] < a[j - 1]) {
                int spray = (a[j - 1] - a[j]);
                cost += spray * b[j];
                a[j] += spray;
            }
        }
        cout << cost << endl;
    }

    return 0;
}