import math

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,input().strip().split(' '))
mod = [0]*k
for x in a:
    mod[x % k] += 1

out = 0
for i in range(1,math.ceil(k/2)):
    out += max(mod[i], mod[k-i])
    
if(k%2==0):    out+=1

if(mod[0]>0): out+=1
print(out)
