import random

import time

run = 32  # *2*2*2*2*2*2*2
print run

# def insertionSort(arr, left, right):
#  
# 
# #     for i in range(left + 1, right + 1):
# #         temp = arr[i];
# #         j = i - 1;
#          
#     for i in range(left + 1, right + 1):
#             key = arr[i]
#             j = i - 1
#          # print(arr[j])
#             if(key < arr[j]) :
#                   
#                  a = binarysearch(arr, key, j, left)
#                  
#                  # time.sleep(3)
#                  k = i
#                  while k > a:
#                      arr[k] = arr[k - 1]
#                      k -= 1
#                  arr[a] = key
# #         
# 
# #         while j >= left and temp < arr[j] :
# #                 arr[j + 1] = arr[j]
# #                 j -= 1
# #                   
# #         arr[j + 1] = temp;
# 
# 
# def binarysearch(arr, key, high, low):
# 
#     
#     mid = 0;
#     while low <= high:
#                  mid = low + (high - low) / 2
#                  mid = int(mid)
#                  if(mid == high):
#                      return mid;
#                  elif(mid == 0):
#                     return mid;
#                  elif((mid >= 0 and arr[mid] == key) or ((arr[mid] > key) and (arr[mid - 1] < key)) or ((mid == 0)and (key < arr[mid]))):
#                      return mid;
#                  elif (mid >= 0 and key < arr[mid]):
#                      high = mid
#                  elif (mid <= high and key > arr[mid]):
#                      low = mid + 1
#                  
#     return mid;


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

 
# Function to do Quick sort
def quickSort(arr, low, high):
   
  """" while low < high:
 pi = partition(arr, low, high)"""
       
  if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
 
# Driver code to test above


def timSort(arr, n):
    
    for i in range(0, n - 1, run):
        quickSort(arr, i, min((i + run - 1), (n - 1)))
   # merge(arr, 0, 31, 63)

   # merge(arr,64,95,127)
   # merge(arr,0,63,127)
    # for i in range(run,n-1,)
#     
    j = run
    l = 0
#     while j < n - 1:
#         mid = l + j - 1;
#         while mid < n - 1:
#             
       
    while j < n - 1:
      #  print ("j----", j)
        mid = l + j - 1;
        while mid < n - 1:
              
       #     print ("mid---", mid)
            r = min((l + (2 * j) - 1), (n - 1))
        #    print("l---", l, " mid---", mid, " r--", r)
            if(mid < r):
         #       print"merge"
                arr1 = arr[:mid]
                arr2 = arr[mid:r]
                print (arr1)
                fastmerge(arr1, arr2)  # (arr, l, mid, r)
              
            l = l + (2 * j)
            mid = l + j - 1;
        l = 0;
          
        j = 2 * j 
        
       # print("last ", "l---", l, " mid---", mid, " r--", r)
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
        
     
def fastmerge(array1, array2):
    merged_array = []
    while array1 or array2:
        if not array1:
            merged_array.append(array2.pop())
        elif (not array2) or array1[-1] > array2[-1]:
            merged_array.append(array1.pop())
        else:
            merged_array.append(array2.pop())
    merged_array.reverse()
    return merged_array     
     
# def cps_merge_sort(array):
#     return cpsmergeSort(array,lambda x:x)
# 
# def cpsmergeSort(array,continuation):
#     n  = len(array)
#     if n <= 1:
#         return continuation(array)
#     left = array[:n/2]
#     right = array[n/2:]
#     return cpsmergeSort (left, lambda leftR:
#                          cpsmergeSort(right, lambda rightR:
#                                       continuation(fastmerge(leftR,rightR))))     

     
def merge(arr, l, m, r):

    # print (l, " ",m," "  ,r)
    n1 = m - l + 1
    n2 = r - m
   # print "heelo"
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
    # print "heelo2"

  #  merge(arr,64,95,127)
   # merge(arr,0,63,127)
#     # for i in range(run,n-1,)
#     j = run
#     l = 0
#     while j < n - 1:
#         print ("j----", j)
#         
#         while l < n - 1:
#             # l=(l+(2*j))
#             
#             mid = l + j - 1;
#             print ("mid---", mid)
#             r = min((l + 2 * j - 1), (n - 1))
#             print("l---",l," mid---",mid," r--",r)
#             if(mid>r=="false"):
#                 merge(arr, l, mid, r)
#             l = l + (2 * j)
#         j = 2 * j   
#     m=(n-1)/2
#     merge(arr, 0, m, n-1)
#     #
#     '''for j in range(run, n - 1, j=2 * j):
       # j = (2 * j)
       
#         print ("j----", j)
#         for l in range (0, n - 1, l + (2 * j)):
#             
#             # l=(l+(2*j))
#             mid = l + j - 1;
#             print ("mid---", mid)
#             r = min((l + 2 * j - 1), (n - 1))
#        ''' 
#           # merge(arr, l, mid, r)
# '''    
#     for j in range(run, n - 1, 2 * j):
#         for l in range(0, n - 1, l + (2 * j)):
#             mid = l + j - 1;
#             r = min((l + 2 * j - 1), (n - 1))
#             merge(arr, l, mid, r)
# '''
# #         
#         
# def merge(arr, l, m, r):
#     # print (l, " ",m," "  ,r)
#     n1 = m - l + 1
#     n2 = r - m
#  
#     # create temp arrays
#     L = [0] * (n1)
#     R = [0] * (n2)
#  
#     # Copy data to temp arrays L[] and R[]
#     for i in range(0 , n1):
#         L[i] = arr[l + i]
#  
#     for j in range(0 , n2):
#         R[j] = arr[m + 1 + j]
#  
#     # Merge the temp arrays back into arr[l..r]
#     i = 0  # Initial index of first subarray
#     j = 0  # Initial index of second subarray
#     k = l  # Initial index of merged subarray
#  
#     while i < n1 and j < n2 :
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#  #
#     # Copy the remaining elements of L[], if there
#     # are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#  
#     # Copy the remaining elements of R[], if there
#     # are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1

# arr = random.sample(range(1, 100000), 30000)
# 
# left = 0;
# right = 4;

 
arr = random.sample(range(1, 10000), 800)
# for i in range(len(arr)):
 #   print (arr[i]) 
start_time = time.clock()
arr.sort()  
# for i in range(len(arr)):
  #  print (arr[i]) 
print ("bie")
print time.clock() - start_time, "seconds"
 
# time.sleep(10)  # [0,9, 11, 12, 13, 0,5, 6, 90 , 77,0,0,98,101,9,8,7,6,5,3,2,1]
arr = random.sample(range(1, 10000), 800)
 
start_time = time.clock()
# insertionSort(arr)
 
print ("my program")
timSort(arr, len(arr))
print time.clock() - start_time, "seconds"
   
#   
# for i in range(len(arr)):
#     print (i, "---", arr[i])
