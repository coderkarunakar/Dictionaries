# #Extract unique Character 
# Extract Unique characters
# Send Feedback
# Given a string S, you need to remove all the duplicates. That means, the output string should contain each character only once. The respective order of characters should remain same, as in the input string.
# Input format:
# The first and only line of input contains a string, that denotes the value of S.
# Output format :
# The first and only line of output contains the updated string, as described in the task.
# Constraints :
# 0 <= Length of S <= 10^8
# Time Limit: 1 sec
# Sample Input 1 :
# ababacd
# Sample Output 1 :
# abcd
# Sample Input 2 :
# abcde
# Sample Output 2 :
# abcde

def remove_duplicates(S):
    unique_chars = set()
    result = []
    #a for loop to iterate through all the characters of elements
    for char in S:
        #if that particular index value is not in the set then you can append this value to result,and add it to the set as well
        if char not in unique_chars:
            result.append(char)

            unique_chars.add(char)
  # here .join method used to join all elements from the iterable and create a string and it return it as an output to the user.python join returns a new string which is the concatination of the other strings in the iterable specified               
    return ''.join(result)

# Reading input
S = input("please enter input").strip()

# Removing duplicates
updated_string = remove_duplicates(S)

# Printing the updated string
print(updated_string)
