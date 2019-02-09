#include<iostream>
#include<limits.h>

#define i64 unsigned long long

using namespace std;

i64 dp[1000][1000];
//pascal's triangle
i64 nCr(int n, int r)
{
       if(n==r) return dp[n][r] = 1;
       if(r==0) return dp[n][r] = 1;
       if(r==1) return dp[n][r] = (i64)n;
       if(dp[n][r]) return dp[n][r];
    return dp[n][r] = nCr(n-1,r) + nCr(n-1,r-1);
}

int main(){
    int m,n;
    cin>>n>>m;
    i64 val,min_pairs,max_pairs,comb;
    
    int each = n/m;
    int r = n%m;
    //if each team has single member
    if(each != 1)
        comb = nCr(each,2);
    else
        comb = 0;
    
    if((each*m) != n){
        if(r != 1)          //if remaining is not single
            val = nCr(r,2);
        else
            val = 0;
            
        min_pairs = comb*m + each*r + val;
    }
    else{
        min_pairs = comb*m;
    }
    
    int temp = n-(m-1);
    if(temp != 1)
        max_pairs = nCr(temp,2);
    else
        max_pairs = 0;
    
    cout<<min_pairs<<" "<<max_pairs;
    
    
    return 0;
}