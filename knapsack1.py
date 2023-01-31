
sack = []
# pt=[18,15,10,7,6,5,3] 
# wt= [4,5,2,7,1,3,1]
pt=[5,10,15,7,8,9,4]
wt=[1,3,5,4,1,3,2]
n=7
sackw=15
ratio = []
# ratio
for i in range(0,n):
    r = pt[i]/wt[i]
    ratio.append(r)
print(ratio,'')
sumweight = sum(sack)
print(sumweight)

def compare():
    maximum = max(ratio)
    for i in range(0,n):
        if maximum == ratio[i]:
            global a
            a = i
            ratio.pop(a)
            return a
print(sackw)
m = 0    
while m<sackw:
    b = compare()        
    if wt[b] + m <= sackw: 
        sack.append(pt[b])
        print(ratio)
        m= m+wt[b]
        pt.pop(b)
        wt.pop(b)
        print(b)
        print(m)
        
    else:
        c=int(sackw - m)
        d = c/wt[b]
        f=wt[b]*d
        m= m+f
        g= pt[b]*d
        sack.append(g)
        wt.pop(b)
p=sum(sack)
print(f"total weight is: {m}")
print(f"total profit is: {p}")

print(f'knapsack is {sack}')
# print(nwt)
# print(sack)
# print(wt,'its old')