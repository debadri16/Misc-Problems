#include<iostream>
#include<limits.h>

#define i64 unsigned long long

using namespace std;


i64 nCr(i64 n)
{
    return n*(n-1)/2;
}

int main(){
    i64 m,n;
    cin>>n>>m;
    i64 val,min_pairs,max_pairs,comb;
    
    i64 each = n/m;
    i64 r = n%m;
    
    comb = nCr(each);
    
    if((each*m) != n){
        min_pairs = nCr(each+1)*r + comb*(m-r);
    }
    else{
        min_pairs = comb*m;
    }
    
    i64 temp = n-(m-1);
    if(temp != 1)
        max_pairs = nCr(temp);
    else
        max_pairs = 0;
    
    cout<<min_pairs<<" "<<max_pairs;
    
    
    return 0;
}
