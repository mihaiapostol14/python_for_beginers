"""
procedura QUICKSORT(A, inf, sup) este
| i← inf
| j← sup
| x← A[(i+j) div 2]
| repeta
| | cat timp (i<sup)/\ (A[i]<x) executa i← i+1
| | cat timp (j>inf) /\ (A[j]>x) executa j← j-1
| | daca i <=j atunci
| | |	t← A[i]; A[i]← A[j]; A[j]← t
| | |	i← i+1; j← j-1
| | |___▄
| pana cand (i>j)
| daca (inf<j) atunci QUICKSORT(A, inf, j)
| daca (i<sup) atunci QUICKSORT(A, i, sup)
|___▄

"""


def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])

# def QUICKSORT(A, inf, sup):
#     i =inf
#     j =sup
#     x= A[i+]