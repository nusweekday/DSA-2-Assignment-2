#Name: Ahmad Zulfahmi Bin Zainal - 2219235 - Section 1
#Assignment 2 : Sorting Level 2,3,4

#level 2
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)

arr = [5, 9, 3, 1, 2, 8, 4, 7, 6]
print("Original array (level 2) :", arr)
bubbleSort(arr)
print("Sorted array (level 2) :", arr)

#level 3
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        print(arr)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [5, 9, 3, 1, 2, 8, 4, 7, 6]
print("Original array (level 3) :", arr)
mergeSort(arr)
print("Sorted array (level 3) :", arr)

#level 4
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        smaller_than_pivot = []
        bigger_than_pivot = []

        for element in arr:
            if element <= pivot:
                smaller_than_pivot.append(element)
            else:
                bigger_than_pivot.append(element)

        print(smaller_than_pivot + [pivot] + bigger_than_pivot)

        return quickSort(smaller_than_pivot) + [pivot] + quickSort(bigger_than_pivot)

arr = [5, 9, 3, 1, 2, 8, 4, 7, 6]
print("Original array (level 4) :", arr)
arr = quickSort(arr)
print("Sorted array (level 4) :", arr)
