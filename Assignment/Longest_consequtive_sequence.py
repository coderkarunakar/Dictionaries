#Longest Consecutive sequence
#Ex:9,1,8,6,3,4,2,7,10,15

#here the consecutive sequence means just we need to find the numerical order in the group of all elements,and in that we need to find out the longest one in the below case the longest consequence seq
#1,2,3,4
#6,7,8,9,10
#15

#1st Approach:
#sort the array and then remove one by one in this approach we will be having nlogn


#Ex:9,1,8,6,3,4,2,7,10,15
#approach :lets initiailize two variables maxlength,start
#here lets put every element i have in the array into the hashmap
#Go to the each element and check in the forward direction and check how many forward elements are there and similarly check in the backward direction the consequtive order and if any order is mismatched then exit similarly check for other elements too in the hashmap 
#compare the each element lenght and finally find the max value lenght 
#Note:if any element is already exist then skip ,initially consider all the values into True then if you have explored that particular value then mark it as false
# here we choose each element as boolean because we dont want to do the redundant work
# 
# 
def longest_consecutive_sequence(nums):
    #checks if nums is empty
    if not nums:
        return 0
        #converts nums list to a set for faster lookup
    num_set = set(nums)
    #initiate the max lenght of consecutive sequence
    max_length = 0
    #iterate through each num in set
    for num in num_set:
        #checks if prev num -1 is not in the set,it means num is the start of a new sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
     # Iterate through consecutive numbers from current_num and increment current_length

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
     # Update max_length if current_length is greater

            max_length = max(max_length, current_length)
        # Return the maximum length of consecutive sequence
    return max_length

# Example usage:
nums = [9,1,8,6,3,4,2]
print("Longest consecutive sequence length:", longest_consecutive_sequence(nums))
 



#Dry run


