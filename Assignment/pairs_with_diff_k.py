#Pairs with difference k
def count_pairs_with_difference_k(arr, n, k):
    frequency = {}
    count = 0
    
    # Count the frequency of each element in the array
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Traverse through the array to find pairs with difference k
    for num in arr:
        # Check if (num - k) or (num + k) exists in the dictionary
        if k != 0:
            if (num - k) in frequency:
                count += frequency[num - k]
            if (num + k) in frequency:
                count += frequency[num + k]
        else:
            if frequency[num] > 1:
                count += frequency[num] - 1
    
    # For every pair, each element is counted twice, so divide by 2
    return count // 2

# Main function to read input and call the function
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    
    result = count_pairs_with_difference_k(arr, n, k)
    print(result)
