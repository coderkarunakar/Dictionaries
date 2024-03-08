#Longest subset with zeroth sum
def longest_zero_sum_subarray(arr):
    sum_map = {}  # Create a hashmap to store cumulative sums and their corresponding indices
    max_length = 0
    curr_sum = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        # If current sum is zero, update max_length to i+1
        if curr_sum == 0:
            max_length = i + 1
        
        # If current sum already exists in the map, update max_length if needed
        if curr_sum in sum_map:
            max_length = max(max_length, i - sum_map[curr_sum])
        else:
            # If current sum is not in the map, store it with its index
            sum_map[curr_sum] = i
    
    return max_length

# Input
N = int(input())
arr = list(map(int, input().split()))

# Function call
print(longest_zero_sum_subarray(arr))
