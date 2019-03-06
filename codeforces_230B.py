import math
#constraints
n = 1000000
###

#sieve of erastotheses
prime = {}
p = 2

while (p * p <= n): 
     
    if p not in prime: 
       
        for i in range(p * p, n+1, p): 
            prime[i] = "composite"
    p += 1
#######################
#print(prime)

N = int(input())

x = map(int, input().split())

for e in x:
    pr = (math.sqrt(e))
    #print(pr)
    if pr not in prime and pr == int(pr) and pr != 1:
        print("YES")
    else:
        print("NO")
        
