def solution(A):
    # Create a set from the array to enable O(1) average time complexity lookups
    num_set = set(A)
    
    # Initialize the smallest positive integer to 1
    smallest_positive = 1
    
    # Loop to find the smallest positive integer not in the set
    while smallest_positive in num_set:
        # Increment smallest_positive by 1 if it's found in the set
        smallest_positive += 1
    
    # Return the smallest positive integer that is not in the set
    return smallest_positive
