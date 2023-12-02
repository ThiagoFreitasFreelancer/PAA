#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;
const int MAX_N = 100;

int N;
int T = 420; // 7 horas * 60 minutos
vector<int> visitTime(MAX_N);
vector<vector<int>> travelTime(MAX_N, vector<int>(MAX_N));
vector<vector<int>> dp(MAX_N, vector<int>(T + 1, -1));

int solve(int currentMuseum, int remainingTime) {
    if (currentMuseum == N) {
        return 0; // Base case: Todos os museus foram visitados
    }

    if (remainingTime < 0) {
        return 0; // Não é possível visitar mais museus
    }

    if (dp[currentMuseum][remainingTime] != -1) {
        return dp[currentMuseum][remainingTime];
    }

    int maxMuseums = solve(currentMuseum + 1, remainingTime); // Não visitar o museu atual

    for (int nextMuseum = 0; nextMuseum < N; ++nextMuseum) {
        int timeSpent = visitTime[nextMuseum] + travelTime[currentMuseum][nextMuseum];
        int result = solve(currentMuseum + 1, remainingTime - timeSpent);
        if (result != -INF) {
            maxMuseums = max(maxMuseums, result + 1);
        }
    }

    return dp[currentMuseum][remainingTime] = maxMuseums;
}

int main() {
    while (true) {
        cin >> N;
        if (N == 0) {
            break;
        }

        fill(visitTime.begin(), visitTime.end(), 0);
        fill(travelTime.begin(), travelTime.end(), vector<int>(MAX_N, 0));
        fill(dp.begin(), dp.end(), vector<int>(T + 1, -1));

        for (int i = 0; i < N; ++i) {
            cin >> visitTime[i];
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> travelTime[i][j];
            }
        }

        int maxMuseums = solve(0, T);

        cout << maxMuseums << endl;
    }

    return 0;
}
