'''
Created on Jun 28, 2018

@author: ATOZ
'''
# Python program for implementation of Insertion Sort
import time
import random


# Function to do insertion sort
def insertionSort(arr):
 
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
 
 
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])

    
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
            if(key < arr[j]) :
                
                a = binarysearch(arr, key, j, 0)
               
                # time.sleep(3)
                k = i
                while k > a:
                    arr[k] = arr[k - 1]
                    k -= 1
                arr[a] = key


def binarysearch(arr, key, high, low):
    
    mid = 0;
    while low <= high:
                 mid = low + (high - low) / 2
                 mid = int(mid)
                 if(mid == high):
                     return mid;
                 elif(mid == 0):
                    return mid;
                 elif((mid >= 0 and arr[mid] == key) or ((arr[mid] > key) and (arr[mid - 1] < key)) or ((mid == 0)and (key < arr[mid]))):
                     return mid;
                 elif (mid >= 0 and key < arr[mid]):
                     high = mid
                 elif (mid <= high and key > arr[mid]):
                     low = mid + 1
                 
    return mid;
    
    '''
    
    mid = low + (high - low) / 2
    mid = int(mid)
   
    if(mid == high):
        return mid;
    elif(mid == 0):
        return mid;
    elif((mid >= 0 and arr[mid] == key) or ((arr[mid] > key) and (arr[mid - 1] < key)) or ((mid == 0)and (key < arr[mid]))):
        return mid;
    elif(mid >= 0 and key < arr[mid]):
        mid = binarysearch(arr, key, mid, low)
    elif(mid <= high and key > arr[mid]):
        # time.sleep(3)
       
        mid = binarysearch(arr, key, high, mid + 1)
    return mid;
    '''

                    
            # Driver code to test above
arr = random.sample(range(1, 1000000), 800000)
# for i in range(len(arr)):
 #   print (arr[i]) 
start_time = time.clock()
arr.sort()  
# for i in range(len(arr)):
  #  print (arr[i]) 
print ("bie")
print time.clock() - start_time, "seconds"

# time.sleep(10)  # [0,9, 11, 12, 13, 0,5, 6, 90 , 77,0,0,98,101,9,8,7,6,5,3,2,1]
arr = random.sample(range(1, 1000000), 800000)

start_time = time.clock()
insertionSort(arr)
print ("my program")
print time.clock() - start_time, "seconds"

# time.sleep(10)
arr = random.sample(range(1, 1000000), 800000)
start_time = time.clock()
insertionSort1(arr)
# print ("Sorted array is:")
# for i in range(len(arr)):
 # print (arr[i])
print ("my program2")
print time.clock() - start_time, "seconds"

