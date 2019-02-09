dp = {};
#pascal's triangle
def nCr(n, r):
    
    dp[n] = {}
    if n==r:
       dp[n][r] = 1
       return 1
    if(r==0):
       dp[n][r] = 1
       return 1
    if(r==1):
       dp[n][r] = n
       return n
    if r in dp[n]:
       return dp[n][r]
       
    dp[n][r] = nCr(n-1,r) + nCr(n-1,r-1)
    return dp[n][r]

def main():
    n,m = map(int,raw_input().split());
    val,min_pairs,max_pairs,comb = 0,0,0,0
    
    each = n//m;
    r = n%m;
    #if each team has single member
    if each != 1:
        comb = nCr(each,2)
    else:
        comb = 0
    
    if (each*m) != n:
        if r != 1:         #if remaining is not single
            val = nCr(r,2)
        else:
            val = 0
            
        min_pairs = comb*m + each*r + val
    
    else:
        min_pairs = comb*m
    
    
    temp = n-(m-1)
    if temp != 1:
        max_pairs = nCr(temp,2)
    else:
        max_pairs = 0
    
    print(min_pairs),
    print(max_pairs)

main()