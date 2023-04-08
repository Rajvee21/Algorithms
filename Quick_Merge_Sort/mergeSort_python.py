def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1+1)
    R = [0] * (n2+1)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] < R[j]:
            print(f"filling index {k} with {L[i]} from left.")
            arr[k] = L[i]
            i += 1
        else:
            print(f"filling index {k} with {R[j]} from right.")
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        print(f"copying index {k} with {L[i]} from left")
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        print(f"copying index {k} with {R[j]} from right")
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    print(f"\nSorting between {l} <-> {r}")
    if l >= r:
        return

    # Same as (l+r)//2, but avoids overflow for
    # large l and h
    m = int((l+r)/2)
    merge(arr, l, m, r)

    # Sort first and second halves
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
   # merge(arr, l, m, r)
 
 
# Driver code to test above
arr = [9,5,7,7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
 