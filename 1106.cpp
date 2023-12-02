#include <iostream>
#include <vector>
#include <iomanip>
#include <cstdlib>

using namespace std;

const int MAXN = 305;
const double EPS = 1e-9;

int N;
double M[MAXN][MAXN];
vector<pair<int, int>> races;
double dp[2 * MAXN][MAXN];

double solve(int race, int winner) {

    if (dp[race][winner] > -1.0) {
        return dp[race][winner];
    }

    int racerB = races[race - (N + 1)].first;
    int racerA = races[race - (N + 1)].second;

    double probA = solve(racerA, winner);
    double probB = solve(racerB, winner);

    return dp[race][winner] = probA * M[racerA][winner] + probB * M[racerB][winner];

}

int main() {
    while (true) {
        cin >> N;

        if (N == 0) {
            break;
        }

        for (int i = 0; i < 2 * MAXN; ++i) {
            for (int j = 0; j < MAXN; ++j) {
                dp[i][j] = -1.0;
            }
        }

        for (int i = 1; i <= N; ++i) {
          for (int j = 1; j <= N; ++j) {
              cin >> M[i][j];
          }
        }

        races.clear();

        for (int i = 0; i < N - 1; ++i) {
            int A, B;
            cin >> A >> B;
            races.push_back({A, B});
        }

        cout << fixed;
        cout.precision(6);
        cout << solve(N + 1, 1) << endl;
    }

    return 0;
}
