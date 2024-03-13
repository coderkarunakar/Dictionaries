#maximum frequency in the given numbers
def max_frequency(arr):
    #created an empty dictionary,to store freq of each element in the input array
    frequency = {}
    #initially initiallizing max freq ele as 0th index value
    max_freq_element = arr[0]
    #traveling in the array
    for num in arr:
        #if already that no exist in the frequency dict then increase by 1 else initialize
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        #this checks if the freq of the current no is greater than the freq of the current max freq element,if it is then max_freq_element is updated to the current num 'num'

        if frequency[num] > frequency[max_freq_element]:
            max_freq_element = num
    #finally return max element 
    return max_freq_element

# Input
n = int(input("enter the no of elements you want to enter"))
arr = list(map(int, input().split("enter the elements")))

# Output
print(max_frequency(arr))
