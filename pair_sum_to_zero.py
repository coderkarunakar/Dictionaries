 #question:pair sum to zero :we need to pair two digits such that its sum = 0 and we can use the already no to pair with other number

def find_pairs_with_sum_zero(arr):
    #this line initializes an empty list ,we will store pairs of numbers that sum upto zero
    pairs = []
    #an empty set used to keep track of already seen numbers while iterating into array
    seen = set()
 #this is for iterating purpose
    for num in arr:
        #calculates the complement of the current no i.e -num,this will be the number when added to num results in zero
        complement = -num
        #this checks the complement is seen in the set
        if complement in seen:
            #if compliment exist in seen this line appends a tuple to the pairs of list,representing a pair of numbers whose sum is zero
            pairs.append((num, complement))
            #this line adds the current number num to the set seen,marking it as seen
        seen.add(num)
#finally returns pairs
    return pairs

# Sample Input
n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Find pairs with sum zero
pairs = find_pairs_with_sum_zero(arr)

# Output the pairs
print("Number of pairs with sum zero:", len(pairs))
print("Pairs:")
for pair in pairs:
    print(pair)
