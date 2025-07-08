import time

strar_time=time.time()


def mergeSort(arr):
    print("out")
    if len(arr) > 1:
        print("step")

        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements
        # into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def bublle_sort( array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Given array is", end="\n")
    printList(arr)
    bublle_sort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    strart_stop =time.time() -strar_time
    print(strart_stop)