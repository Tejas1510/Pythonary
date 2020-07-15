# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(len(b)):
    a1=binary_search(a,0,len(a), b[i])

    sum1=sum1+a1+1
a=a[::-1]
for i in range(len(b)):
    a2=binary_search(a,0,len(a), b[i])

    sum2=sum2+a2+1
print(sum1,sum2)
