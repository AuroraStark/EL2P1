#minSumProduct
def minproduct(a,b,n,k):
    diff,res= 0,0
    for i in range(n):
        p = a[i]*b[i]
        res = res + p
        if (p<0 and b[i]<0):
            temp = (a[i]+2*k)*b[i]
        elif (p<0 and a[i]<0):
            temp = (a[i]-2*k)*b[i]
        elif (p>0 and a[i]<0):
            temp = (a[i]+2*k)*b[i]
        elif (p>0 and a[i]>0):
            temp = (a[i]-2*k)*b[i]
        d = abs(p-temp)
        if d>diff:
            diff = d
        return res-diff
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(minproduct(a,b,n,k))
