#include <iostream>
#include <queue>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    string grid[n];
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    // Find shortest path from bottom left to top right corner using BFS
    queue<pair<int, int>> q;
    q.push({0, 0});
    
    const int INF = 1e9 + 7;
    
    vector<vector<int>> distances(n, vector<int>(n, INF));
    
	distances[0][0] = 0;

	while (!q.empty()) {
		int x = q.front().first, y = q.front().second;
		q.pop();
		
		if (x == n - 1 && y == n - 1) break;

        for (auto [dx, dy] : vector<pair<int,int>>{{1, 0}, {-1, 0}, {0 ,1}, {0 ,-1}}) {
            int nx = x + dx,
                ny = y + dy;

            if (nx < 0 || ny < 0 || nx >= n || ny >= n)
                continue;

            if(grid[nx][ny] == 'M') 
                continue;

			if(distances[x][y]+1<distances[nx][ny]){
				distances[nx][ny]=distances[x][y]+1;
				q.push({nx,ny});
			}
        }
	}

	// Determine whether initial directions can be opposite and find optimal sequence of moves accordingly.
	if(distances[n-2][n-1]!=INF&&distances[n-2][n-1]!=INF){
	    // Initial directions can be opposite. Choose simpler path.
		if(abs(distances[0][n-2]-distances[n-2][n-2])%2==abs(distances[n-2][0]-distances[n-2][n-2])%2) {
			// Both paths have the same parity. Choose one with less steps.
			cout << min(distances[0][n - 2], distances[n - 2][0]) * 9;
		}else{
		    // Paths have different parities. Use formula to calculate number of steps required to reach end point.
			cout<<abs(distances[0][n - 3] + distances[1][n - 2] - distances[0][n - 1] + distances[1][n - 1])*9;
		}
    }else{ 
        // Initial directions cannot be opposite. Just choose simpler path.
        cout << max(distances[0].back(), distances.back()[0]) * 9;
    }
    
	return 0;
}