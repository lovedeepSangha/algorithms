import random
from cProfile import run

run = 32


def insertionSort(arr, left, right): 
    for i in range(left + 1, right + 1):
        temp = arr[i];
        j = i - 1;
        while j >= left and temp < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                
        arr[j + 1] = temp;


def timSort(arr, n):
    
    for i in range(0, n - 1, run):
        insertionSort(arr, i, min((i + 31), (n - 1)))
   # merge(arr, 0, 31, 63)
   # merge(arr,64,95,127)
   # merge(arr,0,63,127)
    # for i in range(run,n-1,)
    j = run
    l = 0
#     while j < n - 1:
#         mid = l + j - 1;
#         while mid < n - 1:
#             
     
    while j < n - 1:
        print ("j----", j)
        mid = l + j - 1;
        while mid < n - 1:
           
            
            print ("mid---", mid)
            r = min((l + (2 * j) - 1), (n - 1))
            print("l---", l, " mid---", mid, " r--", r)
            if(mid < r):
                print"merge"
                merge(arr, l, mid, r)
            
            l = l + (2 * j)
            mid = l + j - 1;
        l=0;
        
        j = 2 * j 
        
        
        print("last ", "l---", l, " mid---", mid, " r--", r)
       # merge(arr, 0, m, n - 1)
        # merge(arr, 0, m, n - 1)

'''for j in range(run, n - 1, j=2 * j):
       # j = (2 * j)
       
        print ("j----", j)
        for l in range (0, n - 1, l + (2 * j)):
            
            # l=(l+(2*j))
            mid = l + j - 1;
            print ("mid---", mid)
            r = min((l + 2 * j - 1), (n - 1))
       ''' 
          # merge(arr, l, mid, r)
'''    
    for j in range(run, n - 1, 2 * j):
        for l in range(0, n - 1, l + (2 * j)):
            mid = l + j - 1;
            r = min((l + 2 * j - 1), (n - 1))
            merge(arr, l, mid, r)
'''
        
     
def merge(arr, l, m, r):
    # print (l, " ",m," "  ,r)
    n1 = m - l + 1
    n2 = r - m
    print "heelo"
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
    print "heelo2"


arr = random.sample(range(1, 100000), 80000)
left = 0;
right = 4;
timSort(arr, len(arr))
for i in range(len(arr)):
   print (i, "---", arr[i])
