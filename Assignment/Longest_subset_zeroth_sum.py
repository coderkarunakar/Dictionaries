#Longest subset with zeroth sum
def longest_zero_sum_subarray(arr):
    #the above line takes list arr as a input
    sum_map = {}  # Create a hashmap(Empty dictionary) to store cumulative sums and their corresponding indices
    max_length = 0
    #initialize maxlenght as 0 to keep track of the max lenght of the subarray with a zero sum.it start with a value of 
    curr_sum = 0
    #this above is to keep  track of the cumulative sum of elements in the array.it start with a value of 0
    
    for i in range(len(arr)):
        #this line starts a loop over each index i in the range from 0 to the length of the input  array arr
        curr_sum += arr[i]
        #this line updates the current sum by adding the value of the element at index i in the input array 'arr'
        
        # If current sum is zero, update max_length to i+1
        if curr_sum == 0:
# This line checks if the curr_sum is equal to zero. If it is, it means that the subarray from index 0 to index i (inclusive) has a zero sum, so it updates max_length accordingly.
            max_length = i + 1
        
        # If current sum already exists in the map, update max_length if needed
        if curr_sum in sum_map:
            max_length = max(max_length, i - sum_map[curr_sum])
            # This line checks if the current cumulative sum curr_sum already exists in the sum_map. If it does, it means there's a subarray with a zero sum starting after the index stored in sum_map[curr_sum]. So it calculates the length of this subarray (by subtracting the current index i from the index stored in sum_map[curr_sum]) and updates max_length if this length is greater than the current max_length.
        else:
            # If current sum is not in the map, store it with its index
            sum_map[curr_sum] = i
            # This line is executed if the current cumulative sum curr_sum is not found in the sum_map. It stores the current cumulative sum curr_sum as a key in the sum_map with its corresponding index i as the value.
    
    return max_length   

# Input
N = int(input())
arr = list(map(int, input().split()))

# Function call
print(longest_zero_sum_subarray(arr))


#Dry run 