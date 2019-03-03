# cook your dish here
T = int(input())

for _ in range(T):
    N, d = map(int, input().split())
    
    s = str(N)
    if len(s) == 1:
        if d<N:
            print(d)
        else:
            print(N)
    else:
        i = 1
        sd = str(d)
        while i <= len(s):
            r = N%(10**i)
            if int(sd) < r:
                N = (N//(10**i))*(10**i) + int(sd)
                sd = sd + str(d)
            else:
                sd = str(r) + str(d)
            i+=1
            
        print(N)