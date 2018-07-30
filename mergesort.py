from test.test_wsgiref import hello_app
def merge(arr, l, m, r):
    #print (l, " ",m," "  ,r)
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

 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) / 2
        #print("mid",m)
        #
        # Sort first and second halves
        mergeSort(arr, l, m)
        #for i in range(l, m,1):
       #     print ( arr[i]),
        #print
        #print "first"    
        #print ("mmm",m,"rrrrr",r)
        mergeSort(arr, m + 1, r)
        
        #print ("2mmm",m+1,"rrrrr",r)
        #for i in range(m, r,1):
         #   print (arr[i]),
        #print
        #print "second"
        #print("low",l,"mid",m,"high",r)
        merge(arr, l, m, r)
      #  print "merge "
        #for i in range(l, r):
         #   print (arr[i]),

       # print ("jhjkhkjhkjhkjh")

        #lovedeep sangha
#9217670670
# Driver code to test above
import random
import time

arr = random.sample(range(1, 1000000), 800000)
n = len(arr)
print ("Given array is")
#for i in range(n):
 #   print ("%d" % arr[i]),
start_time = time.clock()
mergeSort(arr, 0, n - 1)
#print ("\n\nSorted array is")
#for i in range(n):
 #  print ( arr[i])
print time.clock() - start_time, "seconds"