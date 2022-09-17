def insertionSort(a):
    for i in range(1, len(a)):
        num = a[i]
        j = i - 1
        while j >= 0 and num < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = num


def insert_sort(A, n):
    if n ==0:
        return
    insert_sort(A, n-1)
    j =n
    while j>0 and A[j] < A[j-1]:
        A[j],A[j-1] = A[j-1],A[j]
        j-=1
    return A




a = [12, 11, 13, 5, 6, 23, 54, 100, 17, 29, 33]
insertionSort(a)
print(a)