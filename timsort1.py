

run = 32


def merge(arr, l, m, r):
    # print (l, " ",m," "  ,r)
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 #
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def insertionSort(arr, left, right):
    
    for i in range(left + 1, right - 1):
        temp = arr[i];
        j = i - 1;
        while j >= left and temp < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                
        arr[j + 1] = temp;
""" for ( i = left + 1, i <= right, i=i+1):
        
    
        int temp = arr[i];
        int j = i - 1;
        while (arr[j] > temp && j >= left):
        
            arr[j+1] = arr[j];
            j--;
        
        arr[j+1] = temp;
    
"""


def insertionSort1(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
        # print(key)
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        # print(arr[j])
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


def timSort(arr, n):
    
    for i in range(0, n - 1, run):
        insertionSort(arr, i, min((i + 31), (n - 1)))
    
    for j in range(run, n - 1, 2*j):
        for l in range(0, n - 1, l + (2 * j)):
            mid = l + j - 1;
            r = min((l + 2 * j - 1), (n - 1))
            merge(arr, l, mid, r)


arr = [9, 8, 7, 6, 5, 432, 1, 2]
timSort(arr, len(arr))
for i in range(len(arr)):
    print (arr[i])
    
    """// Sort individual subarrays of size RUN
    for (int i = 0; i < n; i+=RUN)
        insertionSort(arr, i, min((i+31), (n-1)));
 
    // start merging from size RUN (or 32). It will merge
    // to form size 64, then 128, 256 and so on ....
    for (int size = RUN; size < n; size = 2*size)
    {
        // pick starting point of left sub array. We
        // are going to merge arr[left..left+size-1]
        // and arr[left+size, left+2*size-1]
        // After every merge, we increase left by 2*size
        for (int left = 0; left < n; left += 2*size)
        {
            // find ending point of left sub array
            // mid+1 is starting point of right sub array
            int mid = left + size - 1;
            int right = min((left + 2*size - 1), (n-1));
 
            // merge sub array arr[left.....mid] &
            // arr[mid+1....right]
            merge(arr, left, mid, right);
        }
    }
}
"""

