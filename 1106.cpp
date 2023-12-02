#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int N;
double prob[301][301], dp[601][301];
vector<int> tree[601];

double solve(int node, int winner) {
    if (node <= N) return (node == winner) ? 1.0 : 0.0;
    if (dp[node][winner] > -0.5) return dp[node][winner];
    double ans = 0.0;

    // Modificação na lógica do cálculo
    for (int i = 1; i <= N; i++) {
        if (i == winner) continue;  // Evita cálculos desnecessários

        double currentProb = prob[i][winner] * solve(tree[node][0], i) * solve(tree[node][1], winner);
        ans = max(ans, currentProb);
        
        currentProb = prob[winner][i] * solve(tree[node][0], winner) * solve(tree[node][1], i);
        ans = max(ans, currentProb);
    }
    return dp[node][winner] = ans;
}

int main() {
    while (cin >> N && N) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                cin >> prob[i][j];
            }
        }
        for (int i = N + 1; i <= 2 * N - 1; i++) {
            tree[i].clear();
            int a, b;
            cin >> a >> b;
            tree[i].push_back(a);
            tree[i].push_back(b);
        }
        for (int i = 1; i <= 2 * N - 1; i++) {
            for (int j = 1; j <= N; j++) {
                dp[i][j] = -1.0;
            }
        }
        cout << fixed << setprecision(6) << solve(2 * N - 1, 1) << endl;
    }
    return 0;
}
