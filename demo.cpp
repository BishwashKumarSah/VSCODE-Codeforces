#include<bits/stdc++.h>
using namespace std;

void solve(int r,int c,int R,int C,vector<vector<int>>& matrix,int& ans,int val){
    if (r == R) return ;
    if (c == C) return ;
    val += matrix[r][c];
    ans = max(ans,val) ;
    solve(r+1,c,R,C,matrix,ans,val);
    solve(r,c+1,R,C,matrix,ans,val);
    val -= matrix[r][c];
}
int main(){
    int N,M;
    cin >> N >> M;
    int ans = INT_MIN;     
    vector<vector<int>> matrix(N, vector<int>(M));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> matrix[i][j];
        }
    }
    solve(0,0,N,M,matrix,ans,0);
    cout << ans << endl;
}

    



