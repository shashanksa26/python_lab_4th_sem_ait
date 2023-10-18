s = input("Enter a: ")
a = [int(x) for x in s.split(",")]
n = len(a)
print(a)
def insertionSort(a):
    for i in range(0, n):
        m = a[i]
        for j in range(i, -1, -1):  
            if m < a[j]:
                a[j+1] = a[j]
                a[j] = m
insertionSort(a)
# print(a)
def mergeSort(a):
    if len(a) == 1:
        return
    # Create a2 <- A[start..mid] and a2 <- A[mid+1..end]
    mid = len(a)//2
    a1 = a[:mid]
    a2 = a[mid:]
    # Sort the two halves
    mergeSort(a1)
    mergeSort(a2)
    # i:a1, j:a2, k:a
    i = j = k = 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            i += 1
        else:
            a[k] = a2[j]
            j += 1
        k += 1
# Copy remaining elements of a1 and a2
    while i < len(a1):
        a[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        a[k] = a2[j]
        j += 1
        k += 1
mergeSort(a)
print(a)