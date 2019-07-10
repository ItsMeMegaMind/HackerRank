import math
l = []
i = 0
j = 0
ind = []
temp = []
temp.append([i,j])
for _ in range(math.ceil(5/2)):
    while j < (5-_ - 1):
        j+=1
        temp.append([i,j])
    while i< (5-_ - 1):
        i+=1
        temp.append([i,j])
    while j> (_):
        j-=1
        temp.append([i,j])
    while (i>_+1):
        i -= 1
        temp.append([i,j])
    ind.append(temp)
    temp = []

unrolled = []
for i in ind:
    a = []
    for j in i:
        a.append(l[j[0]][j[1]])
    unrolled.append(a)
final = []
for _ in unrolled:
    a = [None]*len(_)
    for i in range(len(_)):
        j = (i+k)%((len(_)))
        a[j] = _[i]
    final+=a
print(unrolled)
print(final)
out = [[None]*5]*5
print(ind)
indi = []
for items in ind:
    for _ in items:
        indi.append(_)
print(indi)

for items in indi:
    w = items[0]
    x = items[1]
    p = final.pop(0)
    print(w,x,p)
    out[w][x] = p


print(out)
