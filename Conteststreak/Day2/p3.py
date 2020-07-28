

def findClosest(arr, n, target):
    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]
    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) // 2

        if (arr[mid] == target):
            return arr[mid]

        if (target < arr[mid]) :

            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)


            j = mid


        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)

            i = mid + 1

    return arr[mid]

def getClosest(val1, val2, target):

    return val2

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]

c.append(a[0])
for i in range(1,len(a)):
    c.append(a[i]+c[i-1])


for i in range(len(b)):
    ans=findClosest(c,len(c),b[i])
    ind=c.index(ans)
    if(ind>0):
        print(ind+1,b[i]-c[ind-1])
    else:
        print(ind+1,b[i])
