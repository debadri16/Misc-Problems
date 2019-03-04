#include<iostream>
#include<stdio.h>
#include<vector>
#include <bits/stdc++.h> 
using namespace std;

int main(){
    long n,l,x;
    double d;
    vector<long> a;
    cin>>n>>l;
    for(long i=0;i<n;i++){
        cin>>x;
        a.push_back(x);
    }
    
    sort(a.begin(),a.end());
    
    for(long i=0;i<n;i++){
        if(i == 0){
            d = (double)a[i];
        }
        else{
            x = a[i]-a[i-1];
            if((double)x/2 > d)
                d = (double)x/2;
        }
    }
    //check extention of l
    x = l-a[n-1];
    if((double)x > d)
        d = (double)x;
    
    printf("%lf",d);
    
    return 0;
}
