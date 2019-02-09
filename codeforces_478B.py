def nCr(n):
    return n*(n-1)/2

def main():
    n,m = map(int,raw_input().split());
    val,min_pairs,max_pairs,comb = 0,0,0,0
    
    each = n/m
    r = n%m
    
    comb = nCr(each)
    
    if((each*m) != n):
        min_pairs = nCr(each+1)*r + comb*(m-r)
    
    else:
        min_pairs = comb*m
    
    
    temp = n-(m-1)
    if(temp != 1):
        max_pairs = nCr(temp);
    else:
        max_pairs = 0
    
    print(min_pairs),
    print(max_pairs)

main()