# TO-DO: Complete the selection_sort() function below 
#import math
      
arr = [2,4,6,5,3,7,8,9,1,10]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        #print(i)
        cur_index = i #(temp = arr[i] from the example)
        smallest_index = cur_index  # J = i 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        #Start with the current number
        for j in range(cur_index + 1, len(arr)):
            #arr[j] is refrencing the arr # while j alone is referencing the index. 
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if cur_index < smallest_index:
            arr[cur_index],arr[smallest_index] = arr[smallest_index], arr[cur_index]
            # current_index += 1
           
    return arr
selection_sort(arr)
print(arr)

        #if current_index < smallest_index then hold onto the smallest index and compare the current index to the rest of array
        # Once current_index iterates through length of array, compare to the smallest index

        #if current_index < smallest index, set the current_index to be the smallest index (swap the two out)
        #print smallest_index[i] = current_index
    
        # TO-DO: swap
        #for current_index
   




# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    num_a= arr[i]
    num_b= ar[i + 1]
    j = i
    for j in range(1,2,(len (arr) - 1)):
        if num_a > num_b:
            #set num to the right(b) to num a (swap)
            num_b[i] = num_a[i + 1]
            
            


    return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr